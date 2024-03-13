from __future__ import annotations

from datetime import date

import snowflake.snowpark as sp
import streamlit as st
from snowflake.snowpark.functions import col, date_trunc

from common.utils import get_pandas_df, get_table

TABLE_NAME = "SAMPLE.PUBLIC.EVENT_DATA"


def get_events(table_name: str = TABLE_NAME) -> sp.DataFrame:
    customers = get_pandas_df(
        get_table(table_name).select("customer").distinct(), lowercase_columns=True
    )

    col1, col2 = st.columns(2)

    dates = col1.date_input(
        "Select date range",
        value=[date(2021, 6, 1), date(2021, 12, 29)],
        min_value=date(2021, 1, 1),
        max_value=date(2021, 12, 29),
        key="date_range",
    )

    customer = col2.multiselect(
        "Select customers", customers["customer"].tolist(), key="customers"
    )

    try:
        start, end = dates  # type: ignore
    except ValueError:
        st.error("Please select a valid date range")
        st.stop()

    events = (
        get_table(table_name)
        .select(
            date_trunc("day", "event_time").alias("day"),
            date_trunc("week", "event_time").alias("week"),
            "event_id",
            "customer",
            "user_id",
        )
        .where(col("day").between(start, end))
    )

    if customer:
        events = events.where(col("customer").isin(customer))

    return events
