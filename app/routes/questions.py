from fastapi import APIRouter

router = APIRouter(tags="Questions", routes="/api/questions")


@router.get("/get-questions")
def getQuestions():
    return 