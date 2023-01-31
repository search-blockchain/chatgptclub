CREATE TABLE gpt_answer (
	question TEXT,
	answer TEXT,
	limit_time INTEGER,
	checkout INTEGER
);

CREATE TABLE keywords (
	origin TEXT,
	word TEXT,
	limit_time INTEGER
);

CREATE TABLE question_model (
	prefix TEXT,
	suffix TEXT
, model INTEGER);