SELECT
        op1.email,
        op1.post_id,
        op1.post_slug,
        op1.subject,
        op1.open_date,
        op1.post_date,
        op1.event,
        op1.channel,
        op1.post_opens,
        op1.post_unique_opens,
        op1.previous_opens,
        CASE
            WHEN op1.org IS NULL THEN 'No Org'
            ELSE op1.org END AS org,
        CASE
            WHEN op1.group_customer IS NULL THEN 'No Org'
            ELSE op1.group_customer
        END AS group_customer
FROM
    (
        SELECT
                *,
                (
                SELECT
                        TRIM(reversed_orgs[OFFSET(0)], "\"") AS org
                  FROM
                    (
                        SELECT
                                ARRAY_REVERSE(JSON_EXTRACT_ARRAY(data , "$.user_subscription_notification")) as reversed_orgs
                        FROM `fenix-marketplace-data.firestore_marketplace.user_raw_latest` u
                        WHERE  op.email = JSON_EXTRACT_SCALAR(u.data , "$.user_email")
                    )
                 ) AS org,
                (SELECT
                        CASE
                            WHEN JSON_EXTRACT_SCALAR(data , "$.user_subscription_notification[0]") IN
                            (
                            'marketplace-fenix-trial',
                            'marketplace-friends-of-fenix'
                            ) THEN 'Free'
                            WHEN JSON_EXTRACT_SCALAR(data , "$.user_subscription_notification[0]") = 'marketplace-content-access'
                            THEN 'Content'
                            ELSE 'Paid'
                        END group_customer
                  FROM  `fenix-marketplace-data.firestore_marketplace.user_raw_latest` u
                  WHERE  op.email = JSON_EXTRACT_SCALAR(u.data , "$.user_email")
                ) AS group_customer
        FROM
            (
                SELECT
                        email,
                        post_id,
                        post_slug,
                        CASE
                            WHEN subject IS NULL THEN post_slug
                            ELSE subject
                        END AS subject ,
                        MIN(EXTRACT(DATE FROM TIMESTAMP)) AS open_date,
                        MAX(post_date) AS post_date,
                        event,
                        channel,
                        COUNT(post_id) AS post_opens,
                        COUNT(DISTINCT email) AS post_unique_opens,
                        LAG(COUNT(post_id), 1) OVER (ORDER BY MAX(post_date) DESC) AS previous_opens
                FROM  `fenix-mm-reporting.eventstats.appEvents`
                WHERE
                    email NOT LIKE '%fenix%'
                    AND email NOT LIKE '%dbala%'
                    AND email NOT LIKE '%smartz%'
                    --and subject not in ('[Testing LABS]','[Test]','[Migration Test]')
                    AND EXTRACT(DATE FROM post_date) BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) AND PARSE_DATE('%Y%m%d', @DS_END_DATE)
                    AND
                    (
                    SELECT
                            CASE
                                WHEN JSON_EXTRACT_SCALAR(data , "$.user_subscription_notification[0]") IN
                                (
                                    'marketplace-fenix-trial',
                                    'marketplace-friends-of-fenix'
                                ) THEN 'Free'
                                WHEN JSON_EXTRACT_SCALAR(data , "$.user_subscription_notification[0]") = 'marketplace-content-access'
                                THEN 'Content'
                                ELSE 'Paid'
                            END group_customer
                    FROM `fenix-marketplace-data.firestore_marketplace.user_raw_latest` u
                    WHERE email = JSON_EXTRACT_SCALAR(u.data , "$.user_email")
                    )
                IN UNNEST(@CUSTOMER_TYPE)
                AND event IN ('open', 'delivered', 'click', 'bounce')
                AND channel LIKE 'Marketplace Blast'
                GROUP BY
                1, 2, 3, 4 , 7 , 8
            )
            AS op
    )
    AS op1
ORDER BY
    op1.post_date DESC