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
    import pandas as pd

    valid_emails = [
        "jan.kowalski@gmail.com",
        "krzysztof.nowak@outlook.pl"
    ]
    invalid_emails = [
        "invalid.email",
        "another.invalid.email"
    ]

    # Test valid emails
    valid_df = spark.createDataFrame(
        pd.DataFrame({"email": valid_emails})
    )
    valid_results = valid_df.select(
        is_valid_email(valid_df["email"]).alias("is_valid")
    ).collect()
    for row in valid_results:
        assert row["is_valid"] == True

    # Test invalid emails
    invalid_df = spark.createDataFrame(
        pd.DataFrame({"email": invalid_emails})
    )
    invalid_results = invalid_df.select(
        is_valid_email(invalid_df["email"]).alias("is_valid")
    ).collect()
    for row in invalid_results:
        assert row["is_valid"] == False