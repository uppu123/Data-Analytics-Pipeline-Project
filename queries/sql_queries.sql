-- to create clean attendance table
-- CREATE TABLE attendance_clean AS
-- SELECT 
--   col0 AS student_id,
--   col1 AS event_name,
--   col2 AS attendance_status
-- FROM attendance_csv
-- WHERE col0 != 'student_id';


-- -to create clean events table
-- CREATE TABLE events_clean AS
-- SELECT 
--   col0 AS event_id,
--   col1 AS event_name,
--   col2 AS category,
--   col3 AS event_date
-- FROM events
-- WHERE col0 != 'event_id';




-- select * from attendance_clean limit 10;





-- --Revenue Dashboards
-- SELECT 
--   event_name,
--   SUM(payment_amount) AS total_revenue
-- FROM processed
-- GROUP BY event_name
-- ORDER BY total_revenue DESC;



-- -kpi Dashboards
-- SELECT 
--   (SELECT COUNT(*) FROM processed) AS total_registrations,
--   (SELECT COUNT(*) FROM attendance_clean) AS total_attendance,
--   (SELECT COUNT(*) FROM events_clean) AS total_events,
--   (SELECT SUM(sponsorship_amount) FROM sponsors) AS total_sponsorship;



-- -Event Participation
-- SELECT 
--   event_name,
--   COUNT(*) AS total_participants,
--   ROUND(
--     COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 
--     2
--   ) AS participation_percentage
-- FROM processed
-- GROUP BY event_name
-- ORDER BY total_participants DESC;


---Registered vs actual present
-- SELECT 
--   r.event_name,
--   COUNT(r.student_id) AS total_registered,
--   SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS actual_present
-- FROM processed r
-- LEFT JOIN attendance_clean a 
--   ON r.student_id = a.student_id 
--   AND r.event_name = a.event_name
-- GROUP BY r.event_name
-- ORDER BY total_registered DESC



-- - Revenue per event

-- SELECT 
--   event_name,
--   SUM(payment_amount) AS total_revenue
-- FROM processed
-- GROUP BY event_name
-- ORDER BY total_revenue DESC;


-- -Total Sponsor Contribution
-- SELECT 
--   sponsor_name,
--   SUM(sponsorship_amount) AS total_contribution
-- FROM sponsors
-- GROUP BY sponsor_name
-- ORDER BY total_contribution DESC;


-- Event Profatability
-- SELECT 
--   event_name,
--   COUNT(*) AS participants,
--   SUM(payment_amount) AS revenue,
--   ROUND(SUM(payment_amount)*1.0 / COUNT(*), 2) AS revenue_per_participant
-- FROM processed
-- GROUP BY event_name
-- ORDER BY revenue DESC;


---Overall Financial Summary
SELECT 
  reg.total_registration_revenue,
  sp.total_sponsorship,
  reg.total_registration_revenue + sp.total_sponsorship AS total_revenue
FROM 
  (SELECT SUM(payment_amount) AS total_registration_revenue FROM processed) reg,
  (SELECT SUM(sponsorship_amount) AS total_sponsorship FROM sponsors) sp;
