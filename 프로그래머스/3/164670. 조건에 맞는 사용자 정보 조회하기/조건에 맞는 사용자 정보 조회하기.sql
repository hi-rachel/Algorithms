-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
CONCAT(SUBSTR(TLNO, 1, 3), '-',
 SUBSTR(TLNO, 4, 4),'-',
 SUBSTR(TLNO, 8, 4)
) AS 전화번호
FROM USED_GOODS_USER AS USERS
JOIN USED_GOODS_BOARD AS BOARD
ON USERS.USER_ID = BOARD.WRITER_ID
GROUP BY BOARD.WRITER_ID
HAVING COUNT(BOARD.WRITER_ID) >= 3
ORDER BY USER_ID DESC;
