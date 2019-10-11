### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

  The relationship between `Employee` and `Territory` is Many-to-Many.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

   A document store (like MongoDB) is appropriate when the schema of the data to
   be stored is not clearly defined in advance or may evolve over time. Therefore,
   MongoDB does not adhere to ACID compliance which guarantee validity in the
   event of errors or power failures. There are significant improvements  with
   the newest version of MongoDB on this front.
   MongoDB is appropriate for startups that need to rapidly develop.
   MongoDB is not appropriate when dealing with financial data, such as banks, where
   the data demands high reliability  and integrity.


- What is "NewSQL", and what is it trying to achieve?

  NewSQL is a class of relational database management system that seeks to provide
  the scalability of NoSQL systems while maintaining the ACID guarantees of a traditional database system.
