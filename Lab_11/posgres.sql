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


--inserting array--
CREATE OR REPLACE FUNCTION insert_users(
    usernames VARCHAR[], phones VARCHAR[]
)
RETURNS TABLE(invalid_username VARCHAR, invalid_phone VARCHAR) AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..array_length(usernames, 1) LOOP
        IF phones[i] ~ '^\+?[0-9]{1,15}$' THEN
            INSERT INTO phonebook(username, phone)
            VALUES (usernames[i], phones[i]);
        ELSE
            
            invalid_username := usernames[i];
            invalid_phone := phones[i];
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;





--pagination--
CREATE OR REPLACE FUNCTION paginate_phonebook(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, username varchar, phone varchar) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    ORDER BY id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


--deleting from table--
CREATE OR REPLACE PROCEDURE delete_user_by_value(p_value VARCHAR)

AS $$
BEGIN
    DELETE FROM phonebook WHERE username = p_value;
    IF NOT FOUND THEN
        DELETE FROM phonebook WHERE phone = p_value;
    END IF;
END;
$$ LANGUAGE plpgsql;

select*from phonebook;
