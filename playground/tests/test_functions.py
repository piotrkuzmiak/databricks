from ..utilities.utils import is_valid_email


def test_masking_locations():
    """
    Test that the masking_address function masks the address correctly.
    """
    spark.sql("""
        CREATE OR REPLACE TEMP VIEW masking_locations AS 
        SELECT 'Jeleniogórska' AS address UNION ALL 
        SELECT 'Zamenhoffa' AS address UNION ALL 
        SELECT 'Górki' AS address UNION ALL 
        SELECT 'Głogowska' AS address
    """)
    validation_df = spark.sql("""
        SELECT *
        FROM masking_locations
        WHERE repeat('*', length(address)) != masking_address(address)
    """)

    assert validation_df.count() == 0

def test_email_validation():
    """
    Test that the is_valid_email function correctly identifies valid and invalid email addresses.
    """
    valid_emails = [
        "jan.kowalski@gmail.com",
        "krzysztof.nowak@outlook.pl",]
    invalid_emails = [
        "invalid.email",
        "another.invalid.email"]
    for email in valid_emails:
        assert is_valid_email(email) == True
    for email in invalid_emails:
        assert is_valid_email(email) == False