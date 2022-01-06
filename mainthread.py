from bc import TicToc, FindE


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_e = FindE()
    finding_e.find_euler(10000000)
    e = finding_e.value_of_e()
    print("e = ", e)
    print("TIME = %.6f seconds" % (tt.toc()))
