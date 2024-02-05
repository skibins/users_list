<h1>Documentation: User Management System</h1>

<h2>Functions:</h2>

<h3>delete_user(people_dict):</h3>
<p>This function allows the deletion of a user from the dictionary.</p>
<ul>
<li><strong>Parameters:</strong></li>
  <ul>
    <li><em>people_dict:</em> Dictionary containing user information with user IDs as keys.</li>
  </ul>
<li><strong>Operation:</strong></li>
  <ul>
    <li>The function prompts the user to confirm if they want to delete a user.</li>
    <li>If the user confirms, they are asked to provide the ID of the user they want to delete.</li>
    <li>The function then removes the user from the dictionary based on the provided ID.</li>
    <li>After deletion, the updated list of users is displayed.</li>
  </ul>
</ul>

<h3>find_user(people_dict):</h3>
<p>This function allows searching for a user by their ID in the dictionary.</p>
<ul>
<li><strong>Parameters:</strong></li>
  <ul>
    <li><em>people_dict:</em> Dictionary containing user information with user IDs as keys.</li>
  </ul>
<li><strong>Operation:</strong></li>
  <ul>
    <li>The function prompts the user to enter the ID of the user they want to find.</li>
    <li>If the user is found in the dictionary, their data is displayed.</li>
    <li>If the user is not found, a message indicating so is displayed.</li>
  </ul>
</ul>

<h3>add_new_user(people_dict):</h3>
<p>This function allows the addition of a new user to the dictionary.</p>
<ul>
<li><strong>Parameters:</strong></li>
  <ul>
    <li><em>people_dict:</em> Dictionary containing user information with user IDs as keys.</li>
  </ul>
<li><strong>Operation:</strong></li>
  <ul>
    <li>The function prompts the user to provide details for the new user, including name, age, and sex.</li>
    <li>A unique ID is generated for the new user based on the current number of users in the dictionary.</li>
    <li>The function then creates a new record for the user and adds it to the dictionary.</li>
    <li>The user is asked if they want to add another user.</li>
  </ul>
</ul>

<h2>Usage:</h2>
<p>The script prompts the user to choose an action (find user, delete user, or add user) and provides a user-friendly interface for interacting with the user dictionary. Users can perform these actions repeatedly until they choose to exit the program.</p>

<h2>Termination:</h2>
<p>The program terminates gracefully once the user chooses to exit by typing 'esc' when prompted to choose an action.</p>

<h2>Note:</h2>
<p>This script is designed for educational purposes and may require further customization or validation for use in production environments. Users are encouraged to review and modify the script according to their specific requirements and use cases.</p>
