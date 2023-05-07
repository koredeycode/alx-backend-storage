-- create trigger

DROP TRIGGER IF EXISTS purchase;
DELIMITER $$
CREATE TRIGGER purchase
AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
	-- trigger code
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ;
