from utils import *
from preprocess import *

# *** Train Test Split ***
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3 )


# *** Model Training ***

# Random Forest Clasifier
model = RandomForestClassifier()
model.fit(X_train,Y_train)

# *** Model Evaluation ***

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on test data: ', test_data_accuracy)

