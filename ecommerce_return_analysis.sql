SELECT * FROM ecommerce_returns.ecommerce_data;
USE ecommerce_returns;

-- =====================================================
-- 1. OVERALL RETURN ANALYSIS
-- =====================================================
SELECT
	COUNT(*) As total_orders,
    SUM(case
		WHEN returned = 'Yes' THEN 1
        ELSE 0
	END)AS returned_orders,
    ROUND(
		   100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate
FROM ecommerce_data;

-- =====================================================
-- 2. RETURN ANALYSIS BY PRODUCT CATEGORY
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate
FROM ecommerce_data
GROUP BY category
ORDER BY return_rate DESC;
		
-- =====================================================
-- 3. RETURN ANALYSIS BY REGION
-- =====================================================
SELECT
    region,
    COUNT(*) AS total_orders,
    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate
FROM ecommerce_data
GROUP BY region
ORDER BY return_rate DESC;

-- =====================================================
-- 4. RETURN ANALYSIS BY REASON
-- =====================================================
SELECT
	return_reason,
    COUNT(*) As number_of_returns,
    ROUND(
		100.0 * COUNT(*)/
        (SELECT COUNT(*)
        FROM ecommerce_data
        WHERE returned='Yes'),
        2 
	)percentage_of_returns
FROM ecommerce_data
GROUP BY return_reason
ORDER BY number_of_returns DESC;
    
-- =====================================================
-- 5. RETURN ANALYSIS BY SHIPPING COST
-- =====================================================

SELECT 
	returned,
    count(*) As total_orders,
    round(sum(shipping_cost),2) AS total_shipping_cost,
    round(avg(shipping_cost),2) AS average_shipping_cost
from ecommerce_data
group by returned
order by average_shipping_cost;

-- =====================================================
-- 6. PROFIT MARGIN ANALYSIS BY RETURN STATUS
-- =====================================================
SELECT
    returned,
    COUNT(*) AS total_orders,
    ROUND(AVG(profit_margin), 2) AS average_profit_margin,
    ROUND(SUM(profit_margin), 2) AS total_profit_margin
FROM ecommerce_data
GROUP BY returned
ORDER BY average_profit_margin DESC;

-- =====================================================
-- 7. RETURN STATUS BY DISCOUNT
-- =====================================================

SELECT 
	returned,
    count(*) As total_orders,
    round(sum(discount),2) As Total_discount,
    round(avg(discount),2)*100 As average_discount
from ecommerce_data
group by returned
order by Total_discount;

-- =====================================================
-- 8. RETURN STATUS BY PRODUCT PRICE
-- =====================================================
SELECT 
	returned,
    count(*) As total_orders,
    round(sum(price),2) As total_price,
    round(avg(price),2) As average_price
from ecommerce_data
group by returned
order by total_price;

-- =====================================================
-- 9. RETURN STATUS BY CUSTOMER GENDER
-- =====================================================
SELECT
    customer_gender,
    COUNT(*) AS total_orders,
    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate
FROM ecommerce_data
GROUP BY customer_gender
ORDER BY return_rate DESC;

-- =====================================================
-- 7. CATEGORY-LEVEL COST AND PROFIT ANALYSIS
-- =====================================================
SELECT
    category,
    COUNT(*) AS total_orders,

    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,

    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate,

    ROUND(AVG(shipping_cost), 2) AS average_shipping_cost,
	ROUND(AVG(profit_margin), 2) AS average_profit_margin

FROM ecommerce_data
GROUP BY category
ORDER BY return_rate DESC;

-- =====================================================
-- 8. PRODUCT PRICE RANGE VS RETURN RATE
-- =====================================================

SELECT
    CASE
        WHEN price <= 50 THEN '0-50'
        WHEN price <= 100 THEN '51-100'
        WHEN price <= 200 THEN '101-200'
        WHEN price <= 500 THEN '201-500'
        ELSE '500+'
    END AS price_range,

    COUNT(*) AS total_orders,

    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,

    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate

FROM ecommerce_data
GROUP BY price_range
ORDER BY return_rate;
    
-- =====================================================
-- 9. DELIVERY TIME VS RETURN RATE
-- =====================================================

SELECT 
	delivery_group,
    COUNT(*) AS total_orders,
		
	SUM(CASE 
		WHEN returned='Yes' THEN 1
        ELSE 0
	END) AS returned_orders,
    
    ROUND(
		100.0 * SUM(CASE 
			WHEN returned='Yes' THEN 1
            ELSE 0
		END)/COUNT(*),2
        )AS Return_rate
        
FROM ecommerce_data
GROUP BY delivery_group
ORDER BY Return_rate;
-- =====================================================
-- 10. DISCOUNT RANGE VS RETURN RATE
-- =====================================================

SELECT
CASE
    WHEN discount = 0 THEN '0%'
    WHEN discount<=0.05 THEN '1-5%'
    WHEN discount<=0.10 THEN '5-10%'
    WHEN discount<=0.20 THEN '10-20%'
    ELSE '20-30%'
END AS discount_range,

COUNT(*) AS total_orders,

    SUM(CASE
        WHEN returned = 'Yes' THEN 1
        ELSE 0
    END) AS returned_orders,

    ROUND(
        100.0 * SUM(CASE
            WHEN returned = 'Yes' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS return_rate

FROM ecommerce_data
GROUP BY discount_range
ORDER BY return_rate DESC;

-- =====================================================
-- 11. QUANTITY VS RETURN RATE
-- =====================================================
SELECT 
	quantity,
    COUNT(*) AS total_orders,
    
    SUM(CASE
		WHEN returned='Yes' THEN 1
        ELSE 0
	END)AS returned_orders,
    
	ROUND(
		100.0* SUM(CASE
		WHEN returned='Yes' THEN 1
        ELSE 0
	END)/COUNT(*),2)
    AS return_rate
FROM ecommerce_data
GROUP BY quantity
ORDER BY quantity;

-- =====================================================
-- 12. RETURN REASONS BY PRODUCT CATEGORY
-- =====================================================
SELECT
    category,
    return_reason,
    COUNT(*) AS number_of_returns
FROM ecommerce_data
WHERE returned = 'Yes'
GROUP BY category, return_reason
ORDER BY category, number_of_returns DESC;
    
    