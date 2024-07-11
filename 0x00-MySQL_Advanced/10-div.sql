-- creates a func
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = CAST(a AS FLOAT) / b;
    END IF;
    
    RETURN result;
END $$

DELIMITER ;
