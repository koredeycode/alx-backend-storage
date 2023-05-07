-- create index idx_name_first

CREATE INDEX idx_name_first ON names (SUBSTR(name, 1, 1), score);
