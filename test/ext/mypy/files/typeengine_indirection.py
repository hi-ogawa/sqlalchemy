from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, Mapped

Base = declarative_base()

S1: String = String()
S2 = String()  # It doesn't work without type annotation


class Model(Base):
    __tablename__ = "models"

    s0: str = Column(String())
    s1: str = Column(S1)
    # EXPECTED_MYPY: Incompatible types in assignment (expression has type "Column[String]", variable has type "str")
    s2: str = Column(S2)

    t0: Mapped[str] = Column(String())
    t1: Mapped[str] = Column(S1)
    # EXPECTED_MYPY: Incompatible types in assignment (expression has type "Column[String]", variable has type "Mapped[str]")
    t2: Mapped[str] = Column(S2)

    u0 = Column(String())
    u1 = Column(S1)
    u2 = Column(S2)


# EXPECTED_MYPY: Revealed type is "sqlalchemy.orm.attributes.Mapped[Union[builtins.str, None]]"
reveal_type(Model.u1)

# EXPECTED_MYPY: Revealed type is "sqlalchemy.sql.schema.Column[sqlalchemy.sql.sqltypes.String]"
reveal_type(Model.u2)
