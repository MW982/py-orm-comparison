from sql_alchemy import Country, session


@session
def main(*args, **kwargs):
    session = args[0]
    print(session.query(Country))
    print("HI", args, kwargs)


main()
