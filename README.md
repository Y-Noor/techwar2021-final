QUESTION FOR TECHWAR 2021 (industry level):

Design and implement a restful Banking API (including data model, front and back-end  implementation) for a debit and credit of a credit-card account using suitable framework  Java or Kotlin or.Net, or related frameworks. 
 
Software requirement 
i. You should design the structure of a credit-card account that is unique with a pre-defined  limit allowing users to check available balance on the credit-card account, to debit and  credit the account. 
ii. The credit-card account number should managed and generated by the application. iii. An account should have at least one credit-card associated with it. iv. The application should keep the accounts in memory, no databases involved, use any  
data structure you feel appropriate, you will have to justify your choice of data structure  during your presentation to the panel. 
API should do the following: 
i. Create credit-card account with the id (which should be unique) of the account should be  return to client on success or an error message on failure. 
ii. For sake of simplicity, every time an account is created, at least one credit card should be  associated with the account.  
iii. An account as well as a credit card can be queried, and return info of the balance, and other  info of the credit account if any on success or an error message on failure. iv. A credit card account can be credited (money added to it), the new balance of the credit,  account id and time stamp should be return on success or an error message on failure. v. A credit card can be debited (money removed from it), the new balance of the account,  account id and time stamp should be return on success or an error message on failure. vi. Deactivate a credit card. 
vii. A deactivated credit card cannot be credited, debited, but can be queried for credit history  and available balance. 
Requirements: 
i. You can use Java, .Net, Kotlin or related frameworks. 
ii. Keep it simple and to the point (e.g. no need to implement any authentication, only  implement what has been asked). 
iii. Assume that the API will be invoked by multiple systems and services on behalf of end users. iv. The result should be executable as a standalone program (should not an Application server). v. Prepare a short presentation within allocated time to explain your design & implementation  choice.