-- ============================================
-- HR People Analytics: Workforce Insights
-- Dataset: IBM HR Attrition
-- Author: Your Name
-- ============================================

-- 1. Overall attrition rate
SELECT 
    Attrition,
    COUNT(*) AS employee_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hr_data), 2) AS percentage
FROM hr_data
GROUP BY Attrition;

-- 2. Attrition by Department
SELECT 
    Department,
    Attrition,
    COUNT(*) AS count
FROM hr_data
GROUP BY Department, Attrition
ORDER BY Department;

-- 3. Average monthly income by job role
SELECT 
    JobRole,
    ROUND(AVG(MonthlyIncome), 2) AS avg_income,
    COUNT(*) AS headcount
FROM hr_data
GROUP BY JobRole
ORDER BY avg_income DESC;

-- 4. Job satisfaction distribution
SELECT 
    JobSatisfaction,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hr_data), 2) AS percentage
FROM hr_data
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

-- 5. Attrition by years at company (tenure buckets)
SELECT 
    CASE 
        WHEN YearsAtCompany <= 2 THEN '0-2 years'
        WHEN YearsAtCompany <= 5 THEN '3-5 years'
        WHEN YearsAtCompany <= 10 THEN '6-10 years'
        ELSE '10+ years'
    END AS tenure_bucket,
    Attrition,
    COUNT(*) AS count
FROM hr_data
GROUP BY tenure_bucket, Attrition
ORDER BY tenure_bucket;
