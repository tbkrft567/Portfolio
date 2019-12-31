class SessionsController < ApplicationController
   def create
      @logUser = User.find_by_email(secureUser[:email]).try(:authenticate, secureUser[:password])
      if @logUser
         session[:user_id] = @logUser.id
         p logged?
         redirect_to messages_index_path
      else
         flash[:alert] = ['Invalid Combination']
         p logged?
         redirect_to user_new_path
      end
   end
   def destroy
      reset_session
      redirect_to user_new_path
   end
end
