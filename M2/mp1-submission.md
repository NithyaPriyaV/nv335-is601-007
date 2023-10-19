<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 2/26/2023 2:20:12 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221391469-f60718d5-021c-4b68-947f-4ad53466bcc8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1:Screenshot showing the code of Add Task Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221327442-f5c5d141-cff2-4f39-881d-d4bd48e97888.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SubTask2: Proper added task message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221327675-b09ebc19-6cd2-45a6-b2aa-0645060a59c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SubTask2:  Proper rejected added task message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>I used imported datetime function to update lastActivity with the current datetime value.</div><div><br></div><div>I<br>have placed the entered name, description and due values in the dictionary named<br>task individually.</div><div><br></div><div>I used append function to add the entered dictionary values in the<br>tasks list.</div><div><br></div><div>I used try and except to show that the task was added<br>successfully or rejected.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221391562-328baa2b-c9af-4152-82ab-b56101e5be43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Edited process_update() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div><font color="#6a9955">Using if statement I checked that entered task is within length of&nbsp;</font><span<br>style="color: rgb(106, 153, 85);">tasks in the list and made sure the task doesnt<br>go below zero.</span></div><div><font color="#6a9955">If the code is out of bounds it will print<br>the Task does not exist message which is under else statement.&nbsp; &nbsp;</font></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221392256-dffaa9b7-1025-4963-bb98-5c98a1dd5953.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Updated Task Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221392533-31c92843-e2d4-4a78-a1db-910bf2709f2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the success of update_task()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221392583-710bfbbe-4d59-4699-95c7-bc3e89ffc2db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the failue of update_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>Have taken present_task variable and placed the entered task details in it. took<br>another variable called local values. Placed all the existing local values in a<br>dictionary called local_dict.<div>Used a for loop and checked if the entered value is<br>none or already present in the list. Placed the new value in present_task<br>and updated the last activity with urrent date and time.</div><div>If the task is<br>updated it will display a message as successful else will display message as<br>task not updated.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393339-fa32dff9-8a01-4e38-bb7d-778346654366.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited mark_done() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393084-b42b7305-6455-4d13-b730-3a8f9dcbe575.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the failure of mark_done()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393135-713e934d-41a9-43bd-a5d1-13ffea10213e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the success of mark_done()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>assigned the enetered list of task in a variable named task.&nbsp;</div><div>if index is<br>out of bound prints statement as index doesnot exist.</div><div>if task is already done<br>prints message as already done else when task is done just now, captured<br>the time of now using datetime function.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393441-385fc499-f551-446d-a4f6-78d0f5611187.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited view_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393470-4356da23-14da-45e9-a77c-14f35d7c9da2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the success of view_task()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393527-f70d2733-33fd-45b9-aadd-913766a60a34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the failure of view_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393583-d5ef5ca4-9aae-40be-b6d3-f1656789bea1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of list_tasks() output showing one task STUDY<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393658-01821bfa-c023-4cbd-a790-a45e9a5ddee5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of list_tasks() output showing one task ATTEND CLASS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393698-88207569-3b0d-4111-9ece-9fa351bb50d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of list_tasks() output showing one task EXERCISE<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221394048-0f332300-184d-4f5e-a8b9-64f4c8f7ada6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of delete function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393878-3ff54c9c-def3-4957-b504-586ef5589507.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the list of tasks and also the delete function and list<br>after delete function <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221393973-18f80927-cf9b-4dab-8e5f-91d6bc276cdf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last two actions showing list and delete unsuccessful message as index doesnt exits<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>Used del keyword to delete task from list by index.</div><div>Prints message as The<br>requested task at index {index} has been deleted successfully!!!... .</div><div>If index out of<br>bounds prints message as The index that you entered doesnot exist.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221394178-e7ffe646-e399-48f5-9e4d-74b0d1da86db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Incomplete Tasks Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221394288-45e3eb0a-bbfe-4a42-b5b9-8fdb46720983.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the success of get_incomplete_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>generate a list of tasks where the task is not done</div><div>if the value<br>of the key value of done is false then the task will be<br>appended in the list</div><div>passed that list "-tasks" into list_tasks()</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221396383-df333fd0-b070-4784-b1e8-2b5dc418c8ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited get_overdue_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221396272-339e7473-8a3c-4bc4-88e9-ba72dc0fcfa0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing the success of get_overdue_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>Placed a variable with empty list.</div><div>Used the necessary functions and formats for comparing<br>with due date and present date.</div><div>If task done is true and task due<br>is less than present time then the list will be appended in created<br>empty _tasks list.&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221395071-0a6a0d3a-c69b-4cfd-abac-051d9b18016c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for Get Time Remaining Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221395236-3c54da69-4d01-4a81-9e61-3c27a6f6ce1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the failure of get_time_remaining()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221395160-ba4c8c51-4bec-4e10-86b1-7b7f1bc63f04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the success of get_time_remaining() <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>used the necessary functions and formats for comparing with due date and present<br>date.<div>if due date is greater than present time then the remaining time will<br>be displayed.</div><div>else due date is less than present time then the over due<br>time will be displayed.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221396784-a8f35da0-d31b-4ccf-8190-90cdd0f209ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the saved JSON file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221396982-8d76b295-e1bc-4e8e-b307-d7c3ec8d72ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Git bash screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221397048-1e01cbc1-50ac-4de9-b11f-e8f5cf1b3768.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS CODE SCREENSHOT<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/221396784-a8f35da0-d31b-4ccf-8190-90cdd0f209ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the saved JSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I learnt python recently and still learning and had very hard time to<br>complete the code.<div>I was stuck while implementing dictionaries inside the lists and retrieval<br>of data from that list.</div><div>I had problem implementing the correct syntax for which<br>I got it clarified with the professor.</div><div>The remaining function had different formats of<br>the date and time of present date time with due date time. I<br>searched a lot from the materials to solve the remaining function.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/vb437" target="_blank">Grading</a></td></tr></table>