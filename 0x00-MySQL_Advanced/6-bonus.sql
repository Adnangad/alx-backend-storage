-- creates a stored procedure
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name NVARCHAR(255), IN score INT)
BEGIN
    -- Insert into projects table if project_name does not exist
    INSERT INTO projects(name)
    SELECT project_name FROM dual
    WHERE NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name LIMIT 1);

    -- Insert into corrections table
    INSERT INTO corrections(user_id, project_id, score)
    VALUES (
        user_id,
        (SELECT id FROM projects WHERE name = project_name),
        score
    );
END $$

DELIMITER ;
