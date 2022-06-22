import pandas as pd


def final_data(test, delta, match):
    """
    :param test: test data
    :param delta: calculated delta
    :param match: calculated dmatch
    :return:
    """
    try:
        dict = {
            "X (test func)": test.x,
            "Y (test func)": test.y,
            "Delta Y (test func)": delta,
            "No. of ideal func": match,
        }

        return pd.DataFrame(dict)

    except Exception as e:
        print("Error! Code: {c}, Message, {m}".format(c=e.code, m=str(e)))
