# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xlabel(diabetes.feature_names[2])
plt.ylabel('disease progression')
plt.xticks(())
plt.yticks(())

