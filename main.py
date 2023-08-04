from paper_solve import PaperSM
from home_page_work import Penting, Subject, PrSolver

print("start")
if __name__ == "__main__":
    def strt():
        pending_object = Penting()
        sub_object = Subject()

        sub_object.home_page()
        pp = pending_object.total_pending()
        if pp != "0":
            PrSolver().conti_all()
            PaperSM().paper_solver()
            print("pp print", pp)
            strt()

        else:
            print("no pending", pp)


    strt()
