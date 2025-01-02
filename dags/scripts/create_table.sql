CREATE TABLE IF NOT EXISTS daily_news(
    category VARCHAR(15),
    article_id VARCHAR(100) PRIMARY KEY,
    title VARCHAR(1000),
    description VARCHAR(10000),
    link VARCHAR(600),
    pub_date DATE,
    pub_time TIME,
    source_name VARCHAR(200),
    country VARCHAR(100),
    image_url VARCHAR(400),
    video_url VARCHAR(200),
    word_count FLOAT,
    sentiment VARCHAR(20),
    sentiment_score FLOAT  
    );

        
