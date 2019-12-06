# Project 3

I will only discribe the files I have crated/used to help with brevaty 
> orders > views.py: has functions and classes of views 
>orders> urls: redirects values to the particular functions above
>pizza>settings : installed maduals 
>pizza>urls > connects the urls for the whole project 

>static_env: has all my staitc files 
>templates: 
	>account: holds the temps for account(login.html)
	>checkout_page.html: template for check out
	>home_page.html: the landing page 
	>.layout.html: skeleton
	>order_summary.html: view of the cart
	>product_page.html: detail view of the single time


functionality checklist: 

* [X]Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.

* [X]Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.

* [X]Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.

* [X]Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.

* [X]Personal Touch: Add at least one additional feature of your choosing to the web application. Possibilities include: allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders, integrating with the Stripe API to allow users to actually use a credit card to make a purchase during checkout, or supporting sending users a confirmation email once their purchase is complete. If you need to use any credentials (like passwords or API credentials) for your personal touch, be sure not to store any credentials in your source code, better to use environment variables!



My personal touch is implementing Pagination and page count. 



==========. 

The above are my project 3 implementtation  
Below are my additions to project 3 for the final project   

===========.  
Added functionality:   
# 1: Add to the card:    #
![Screen Shot 2019-12-05 at 6 40 14 PM](https://user-images.githubusercontent.com/6343949/70291068-e439a780-178e-11ea-968a-4aee40f772c9.png)
/


# 2: Remove from the card:#   
![Screen Shot 2019-12-05 at 6 40 14 PM](https://user-images.githubusercontent.com/6343949/70291068-e439a780-178e-11ea-968a-4aee40f772c9.png)
/

# 3: Add messages:  #
![image](https://user-images.githubusercontent.com/6343949/70291154-3084e780-178f-11ea-9bd4-ebefb72998f5.png)
/
# 4: Add number of how many items are in the card:  # 
![Screen Shot 2019-12-05 at 5 31 17 PM](https://user-images.githubusercontent.com/6343949/70291216-5ad6a500-178f-11ea-9232-bf8fddb2bab0.png)
/
# 5: Added check out button and check out form:  # 

![Screen Shot 2019-12-05 at 6 45 39 PM](https://user-images.githubusercontent.com/6343949/70291250-73df5600-178f-11ea-8483-4c6981460a32.png)
/
# 6: Added: check out form:   #
![Screen Shot 2019-12-05 at 6 47 49 PM](https://user-images.githubusercontent.com/6343949/70291362-cb7dc180-178f-11ea-98ab-fcb650baea46.png)
/
# 7: Added continue shopping route:  #

![Screen Shot 2019-12-05 at 6 45 39 PM](https://user-images.githubusercontent.com/6343949/70291250-73df5600-178f-11ea-8483-4c6981460a32.png)
/

# 8: added buttonts to chance quentities on order  summary page: # 
![Screen Shot 2019-12-05 at 6 46 15 PM](https://user-images.githubusercontent.com/6343949/70291284-89548000-178f-11ea-97bc-9fedd7331a2d.png)
# 9: Added trash can:   #
![Screen Shot 2019-12-05 at 6 46 48 PM](https://user-images.githubusercontent.com/6343949/70291313-a0936d80-178f-11ea-9af8-f0fd1047030c.png)






