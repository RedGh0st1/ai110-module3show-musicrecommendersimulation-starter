# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

**Catalog Density Creates a Lo-Fi Filter Bubble.**
The 25-song catalog contains three lo-fi tracks but only one song each for 20 other genres, including rock, jazz, classical, and metal. Because the genre match bonus applies to every song in a genre, a lo-fi listener is guaranteed to see three genre-matched songs in their top results simply because of catalog count — not because the system found a better fit. A rock listener, by contrast, has only one song that can ever earn a genre match, so if that single song scores poorly on energy or valence, their top five fills with genre-miss songs that the system settled for. This means recommendation quality is directly tied to how many songs represent a genre in the catalog, which is an accident of data collection rather than a reflection of musical compatibility. In practice, this would push the system to continuously recommend lo-fi to lo-fi listeners while leaving listeners of underrepresented genres with noticeably weaker, more generic results — a classic filter bubble that reinforces what is already well-represented rather than serving the full range of users equally.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**Profiles Tested.**
Nine user profiles were run against the 25-song catalog: three standard profiles (High-Energy Pop, Chill Lo-Fi, Deep Intense Rock) and six adversarial profiles designed to stress-test the scoring logic. The adversarial profiles included The Contradiction (high energy paired with a sad mood preference), The Genre Ghost (a genre not present in the catalog), The Agnostic (every numeric target set to the neutral midpoint of 0.5), The Minor Happy (a cheerful mood preference paired with a minor-key preference), The Lyric Lover (a user who wants fully instrumental music), and The Mismatch Maximizer (extreme preferences designed to push most songs toward a score of zero). Beyond profile testing, two structural experiments were run: a weight shift that doubled the importance of energy and halved the importance of genre, and a feature removal test that disabled the mood signal entirely to observe what the remaining signals would recommend on their own.

**What We Looked For.**
For each profile the evaluation checked whether the top-ranked song was intuitively correct, whether the score breakdown explained the ranking in a way a real listener would recognize as fair, and whether any song appeared in the top five for reasons that felt accidental rather than meaningful.

**What Surprised Us.**
The most unexpected result came from the High-Energy Pop profile. Gym Hero ranked first even though its mood is tagged as "intense" rather than "happy" — the user's stated preference. It won because a subgenre match ("dance pop") awards more points than a mood match, so a song that felt right on paper but wrong in practice claimed the top spot. A pop dance song labeled "intense" is arguably still a good recommendation, but the system arrived there for the wrong reason: it never evaluated whether intense and happy are compatible moods, only whether the subgenre string matched exactly.

The Genre Ghost profile produced the second notable surprise. Before the genre mapping fix was in place, a user who preferred "bossa nova" received recommendations with no connection to jazz whatsoever, and the score output gave no indication that anything had gone wrong. The system silently defaulted to whichever songs scored well on energy and mode, which happened to include a lo-fi track and an ambient track. Adding a genre map fixed the top result immediately, but the experience of running the broken version made clear how invisible catalog gaps are to a user reading a ranked list.

The weight shift experiment produced a result that was surprising in a different way. When energy was made twice as important and genre was halved, a salsa song (Salsa Fuego) entered the top five for a pop listener purely because its energy value was a perfect numerical match. The recommendation was technically defensible — the energy score was higher than any other song in the catalog — but recommending salsa to someone who said their favorite genre is pop illustrates that numerical accuracy and genuine musical fit are not the same thing. A number can be right while the recommendation is wrong.

Finally, removing the mood signal entirely had almost no effect on the Chill Lo-Fi profile. The top three songs remained identical. This revealed that mood was functioning as a small additive bonus in that profile rather than a meaningful differentiator — the genre and energy signals were already doing all the sorting work, and mood was decorative. That was not expected going in, and it raises the question of whether mood is earning its place in the scoring formula for listeners whose genre preference already implies a mood.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
