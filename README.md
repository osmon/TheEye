# TheEye
The Eye is based on Django Rest Framework module. it has django module with an endpoint called EventProcessorAPI wich has 2 methods for attending requests
 1)"store_event": This method store an event that has been sent.
 2)"get_event": In order to the user get the requested events data, a client application need to consult the API sending a JSON with the field "action" filled 
                with one of the next options:
                
                A) session: The user can get events according to a session id. 
                B) category: Users get all the events of given category.
                C) date-range: users have to send a range of dates to filter the events between thos dates.
                
                All the 3 methods return a dictionary with the relevant information and data.
 
The API is waiting for a POST and "CLIENT_KEY" value, if the user does not send the valid key it is going to return a 401 error, indicating that it was a unauthorized request. 

All the data are been stored in SQLite file using 5 different models: FormModel,PayloadModel,CategoryModel,EventModel,CaterogyFieldsModel
