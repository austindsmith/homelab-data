CREATE TABLE IF NOT EXISTS water_payment_history (
  confirmation_no  text PRIMARY KEY,
  account_number   text,
  bill_date        date,
  due_date         date,
  service_address  text,
  amount_due       numeric(12,2),
  payment_method   text,
  payment_date     date,
  payment_amount   numeric(12,2),
  total_amount     numeric(12,2),
  status           text
);
