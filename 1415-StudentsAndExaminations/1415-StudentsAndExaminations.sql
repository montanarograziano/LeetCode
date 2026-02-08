-- Last updated: 08/02/2026, 14:27:57
# Write your MySQL query statement below
select a.student_id, a.student_name, c.subject_name, count(b.student_id) as attended_exams
from Students a
CROSS JOIN Subjects c
LEFT JOIN Examinations b on a.student_id = b.student_id and c.subject_name = b.subject_name
group by 1, 2, 3
order by 1, 2, 3
