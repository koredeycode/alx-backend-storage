-- create the AddBonus procedure

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE user_score INT;
	DECLARE user_projects INT;

	SELECT SUM(score) INTO user_score FROM corrections WHERE corrections.user_id = user_id;
	SELECT COUNT(*) INTO user_projects FROM corrections WHERE corrections.user_id = user_id;
	UPDATE users
	SET users.average_score = IF(user_projects = 0, 0, user_score / user_projects) WHERE users.id = user_id;
END $$
DELIMITER ;
