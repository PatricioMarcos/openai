from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Respuestas predefinidas del chatbot
responses = {
    "hello": "Hello! How can I assist you today?",
    "advice_diet": "To improve your diet, aim for a variety of foods from all food groups. Incorporate more fruits, vegetables, lean proteins like chicken or tofu, and whole grains such as brown rice or quinoa. Try to reduce your intake of processed foods and sugary drinks.",
    "advice_snacks": "Preparing quick, healthy snacks ahead of time can help you avoid reaching for processed options. Consider packing nuts, fruits, or yogurt as snacks.",
    "advice_cravings": "To manage cravings, try incorporating more fiber-rich foods into your meals to help you feel fuller longer. Drinking plenty of water throughout the day can also help reduce cravings.",
    "advice_stress": "Managing stress is crucial for overall health. Consider incorporating stress-relieving activities like yoga, meditation, or deep breathing exercises into your routine.",
    "advice_exercise": "Start with activities you enjoy, such as brisk walking, swimming, or dancing. Setting realistic goals and gradually increasing intensity can help maintain motivation.",
    "goodbye": "You're welcome! Remember, I'm here to support you on your health journey. Don't hesitate to ask for advice anytime.",

    # Películas
    "movies_recommend": "I can recommend some great movies! For example, 'Inception' is fantastic if you enjoy complex plots and stunning visuals.",
    "movies_genre": "I don't have a favorite movie genre, but I appreciate films that explore human conditions and emotional experiences.",
    "movies_remakes": "Remakes can offer a fresh perspective, but they often face comparisons with the originals. Execution and respect for the original work are critical.",
    "movies_best_recently": "Although I don't watch movies, 'The Shawshank Redemption' is highly regarded for its narrative and memorable performances.",
    "movies_production_design": "Movies like 'Blade Runner 2049' are praised for their impressive visual design and world-building.",

    # Clima
    "weather_preferences": "I don't have weather preferences, but I understand how weather impacts health and mood.",
    "weather_diet_adaptation": "Diets can adjust with seasons. For instance, consume more fluids in hot weather and opt for warm foods in cold weather.",
    "weather_best_exercise_season": "Spring and fall are ideal for outdoor exercises due to moderate temperatures and lower humidity.",
    "weather_sleep_quality": "Extreme weather can affect sleep quality. Keeping the room cool and well-ventilated promotes better rest.",
    "weather_adapt_sudden_changes": "Staying informed about weather forecasts and adjusting clothing and diet as needed helps adapt to sudden weather changes.",

    # Salud
    "health_lifestyle_tips": "I recommend a balanced diet, regular exercise, stress management, and adequate rest for overall health.",
    "health_stress_reduction": "Practice relaxation techniques like meditation, yoga, or deep breathing to reduce stress.",
    "health_heart_healthy_foods": "Reducing saturated fats, sodium, and added sugars promotes heart health. Opt for fresh and natural foods.",
    "health_quality_sleep_importance": "Adequate sleep is crucial for physical and mental health. It aids in muscle recovery, memory consolidation, and emotional balance.",
    "health_antioxidant_rich_foods": "Foods like berries, nuts, and leafy greens are rich in antioxidants that combat cellular damage and promote overall health.",

    # Viajes
    "travel_destination_recommend": "If you enjoy historical sites, consider visiting Rome or Athens. Both cities offer rich cultural experiences.",
    "travel_packing_tips": "Pack light and versatile clothing. Consider the weather and activities planned for your trip.",
    "travel_budget_advice": "Create a budget for accommodations, meals, and activities. Look for deals and prioritize experiences that matter most to you.",
    "travel_solo_tips": "Solo travel can be rewarding! Plan ahead, stay informed about safety measures, and embrace the opportunity to meet new people.",
    "travel_language_barrier": "Learning basic phrases in the local language can enhance your travel experience. English is commonly spoken in many tourist destinations.",

    # Tecnología
    "tech_latest_gadgets": "The latest gadgets often include advancements in AI, virtual reality, and smart home technology.",
    "tech_cyber_security_tips": "Protect your online accounts with strong passwords and enable two-factor authentication. Be cautious of phishing scams and update your software regularly.",
    "tech_future_technology_trends": "Future technology trends may include quantum computing, biotechnology, and sustainable energy solutions.",
    "tech_best_productivity_apps": "Productivity apps like Trello, Evernote, and Slack can help you organize tasks, collaborate efficiently, and stay focused.",
    "tech_video_game_recommendation": "If you enjoy strategy games, 'Civilization VI' offers deep gameplay and historical context.",

    # Libros
    "books_recommendation": "For an inspiring read, 'The Alchemist' by Paulo Coelho offers wisdom and a journey of self-discovery.",
    "books_genre_preference": "I don't have a genre preference, but literature that explores human nature and societal issues often makes for thought-provoking reads.",
    "books_best_sellers": "Best-sellers like 'Becoming' by Michelle Obama resonate with readers for their compelling narratives and insights.",
    "books_classics": "'Pride and Prejudice' by Jane Austen remains a classic for its witty social commentary and memorable characters.",
    "books_reading_tips": "Create a reading routine, explore diverse genres, and join book clubs to discuss and discover new perspectives.",

    # Música
    "music_genre_favorite": "I don't have a favorite music genre, but I appreciate music that evokes emotions and inspires creativity.",
    "music_recommendation": "If you enjoy indie folk, 'Bon Iver' offers haunting melodies and introspective lyrics.",
    "music_concert_experience": "Live concerts provide a unique atmosphere to connect with artists and fellow music enthusiasts.",
    "music_playlist_creation": "Create playlists based on mood or activity to enhance your listening experience. Discover new artists and genres along the way.",
    "music_instrument_learning": "Learning an instrument fosters creativity and improves cognitive skills. Start with basics and enjoy the journey of musical exploration.",

    # Deportes
    "sports_fitness_tips": "Incorporate strength training, cardio exercises, and flexibility routines for overall fitness and health.",
    "sports_favorite_team": "I don't have a favorite sports team, but the dedication and teamwork in sports are admirable.",
    "sports_best_events": "Major events like the Olympics showcase athleticism and cultural diversity on a global stage.",
    "sports_training_advice": "Set specific goals, track progress, and seek guidance from fitness professionals to optimize your training regimen.",
    "sports_outdoor_activities": "Outdoor activities like hiking, cycling, and rock climbing offer physical challenges and opportunities to connect with nature.",

    # Bienestar mental
    "mental_health_importance": "Prioritize mental health through self-care practices, social connections, and professional support when needed.",
    "mental_health_coping_strategies": "Develop coping strategies such as mindfulness, journaling, or talking to a trusted person during challenging times.",
    "mental_health_self_reflection": "Reflect on emotions, thoughts, and experiences to gain insights and foster personal growth.",
    "mental_health_reduce_anxiety": "Practice relaxation techniques like deep breathing or progressive muscle relaxation to manage anxiety symptoms.",
    "mental_health_seek_help": "Seeking help from mental health professionals is a proactive step toward emotional well-being and resilience."
}

# Estado inicial del chatbot
current_state = "hello"

def chatbot_response(user_input):
    global current_state

    user_input_lower = user_input.lower()

    if "hello" in user_input_lower or "hi" in user_input_lower or "hey" in user_input_lower:
        current_state = "hello"
        return responses["hello"]
    elif "diet" in user_input_lower or "improve diet" in user_input_lower or "healthy eating" in user_input_lower:
        current_state = "advice_diet"
        return responses["advice_diet"]
    elif "snacks" in user_input_lower or "healthy snacks" in user_input_lower or "snacking" in user_input_lower:
        current_state = "advice_snacks"
        return responses["advice_snacks"]
    elif "cravings" in user_input_lower or "manage cravings" in user_input_lower or "reduce cravings" in user_input_lower:
        current_state = "advice_cravings"
        return responses["advice_cravings"]
    elif "stress" in user_input_lower or "manage stress" in user_input_lower or "stress-relief" in user_input_lower:
        current_state = "advice_stress"
        return responses["advice_stress"]
    elif "exercise" in user_input_lower or "start exercising" in user_input_lower or "exercise routine" in user_input_lower:
        current_state = "advice_exercise"
        return responses["advice_exercise"]
    elif "bye" in user_input_lower or "goodbye" in user_input_lower or "thank you" in user_input_lower:
        current_state = "goodbye"
        return responses["goodbye"]
    elif "movies" in user_input_lower or "film" in user_input_lower or "cinema" in user_input_lower:
        current_state = "movies_recommend"
        return responses["movies_recommend"]
    elif "weather" in user_input_lower or "climate" in user_input_lower or "temperature" in user_input_lower:
        current_state = "weather_preferences"
        return responses["weather_preferences"]
    elif "health" in user_input_lower or "wellness" in user_input_lower or "fitness" in user_input_lower:
        current_state = "health_lifestyle_tips"
        return responses["health_lifestyle_tips"]
    elif "travel" in user_input_lower or "vacation" in user_input_lower or "trip" in user_input_lower:
        current_state = "travel_destination_recommend"
        return responses["travel_destination_recommend"]
    elif "tech" in user_input_lower or "technology" in user_input_lower or "gadgets" in user_input_lower:
        current_state = "tech_latest_gadgets"
        return responses["tech_latest_gadgets"]
    elif "books" in user_input_lower or "literature" in user_input_lower or "reading" in user_input_lower:
        current_state = "books_recommendation"
        return responses["books_recommendation"]
    elif "music" in user_input_lower or "songs" in user_input_lower or "genres" in user_input_lower:
        current_state = "music_genre_favorite"
        return responses["music_genre_favorite"]
    elif "sports" in user_input_lower or "fitness" in user_input_lower or "exercise" in user_input_lower:
        current_state = "sports_fitness_tips"
        return responses["sports_fitness_tips"]
    elif "mental health" in user_input_lower or "wellbeing" in user_input_lower or "self-care" in user_input_lower:
        current_state = "mental_health_importance"
        return responses["mental_health_importance"]
    else:
        # Respuesta por defecto si no se reconoce la pregunta específica
        return "I'm sorry, I didn't quite get that. Could you please ask again or specify your question?"

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = chatbot_response(user_input)
        return jsonify({"bot_response": bot_response})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

