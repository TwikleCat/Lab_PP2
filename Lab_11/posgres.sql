--function--
CREATE OR REPLACE FUNCTION search_phonebook(pattern varchar)
RETURNS TABLE(id INT, name varchar, phone varchar)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook as p
    WHERE p.username ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

--inserting procedur
CREATE OR REPLACE PROCEDURE proc(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE username = p_name;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


select*from phonebook;