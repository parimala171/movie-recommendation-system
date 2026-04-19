from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

movies = pickle.load(open("model.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]

    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = [movies.iloc[i[0]].title for i in movie_list]
    return recommendations

@app.route("/")
def home():
    return "Movie Recommendation API Running"

@app.route("/recommend", methods=["POST"])
def recommend_api():
    data = request.get_json()
    movie = data["movie"]

    result = recommend(movie)

    return jsonify({
        "Recommendations": result
    })

if __name__ == "__main__":
    app.run(debug=True, port=5007)