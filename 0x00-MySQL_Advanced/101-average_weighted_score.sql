-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DROP FUNCTION IF EXISTS Computoor;
DELIMITER $$
CREATE FUNCTION Computoor(user_id INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE total_weighted_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
	DECLARE result INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight)
        INTO total_weight
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

	SET result = IF(total_weight = 0, 0, total_weighted_score / total_weight);
	RETURN result;
END $$
DELIMITER ;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users SET users.average_score = Computoor(users.id);
END $$
DELIMITER ;
