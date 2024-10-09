from sqlmodel import SQLModel, create_engine, Session
from models.blog import Blog


sqlite_file_name = "database.db"  # テーブル名
sqlite_url = f"sqlite:///{sqlite_file_name}"  # エンジンデータベースのURL

# echo=Trueにすることで、すべてのSQL実行時に標準出力にSQL本文が表示
engine = create_engine(sqlite_url, echo=True)  # engineを作成


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  # モデルからテーブルを生成


if __name__ == '__main__':
    create_db_and_tables()
    
def get_session():
    with Session(engine) as session:
        yield session