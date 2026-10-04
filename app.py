import joblib

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="VinoLab AI",
    description="Wine Quality Prediction using Linear Regression",
    version="1.0.0"
)


# ============================================================
# STATIC FILES
# ============================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ============================================================
# TEMPLATES
# ============================================================

templates = Jinja2Templates(
    directory="templates"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("lr_wine_quality.joblib")


print("========================================")
print("VinoLab AI")
print("Wine Quality Prediction Model Loaded")
print("========================================")


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": None
        }
    )


# ============================================================
# PREDICTION
# ============================================================

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,

    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...)
):

    # ========================================================
    # INPUT DATA
    # ========================================================

    input_data = [[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
    ]]


    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = float(
        model.predict(input_data)[0]
    )


    # Keep score within the wine-quality scale
    display_score = max(0, min(10, prediction))


    # ========================================================
    # QUALITY CLASSIFICATION
    # ========================================================

    if display_score < 4:
        quality_label = "Poor"
        quality_message = "This sample has a relatively low predicted quality."

    elif display_score < 6:
        quality_label = "Average"
        quality_message = "This sample has an average predicted quality."

    elif display_score < 7:
        quality_label = "Good"
        quality_message = "This sample shows a good predicted quality profile."

    else:
        quality_label = "Excellent"
        quality_message = "This sample has a high predicted quality."


    # ========================================================
    # RETURN RESULT
    # ========================================================

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": display_score,
            "quality_label": quality_label,
            "quality_message": quality_message
        }
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )