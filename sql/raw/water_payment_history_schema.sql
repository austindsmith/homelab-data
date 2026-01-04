CREATE TABLE IF NOT EXISTS raw.water_payment_history (
  account_number   text,
  bill_date        text,
  due_date         text,
  service_address  text,
  amount_due       text,
  confirmation_no  text,
  payment_method   text,
  payment_date     text,
  payment_amount   text,
  total_amount     text,
  status           text
);