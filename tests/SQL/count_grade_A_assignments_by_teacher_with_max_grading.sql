WITH graded_assignments AS (
    SELECT 
        teacher_id,
        COUNT(*) AS graded_count
    FROM assignments
    WHERE grade = 'A'
    GROUP BY teacher_id
), max_graded_teacher AS (
    SELECT 
        teacher_id
    FROM graded_assignments
    ORDER BY graded_count DESC
    LIMIT 1
)
SELECT 
    COUNT(*) AS count_grade_A_assignments
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM max_graded_teacher);



