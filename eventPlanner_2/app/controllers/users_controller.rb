class UsersController < ApplicationController
  def update
    @user = current_user
    @user.update(first_name: secureUser[:first_name],last_name: secureUser[:last_name],location: secureUser[:location],email: secureUser[:email], state: secureUser[:state])
    if @user.valid?
      redirect_to events_index_path
    else
      flash[:alert] = @user.errors.full_messages
      redirect_to users_edit_path(current_user.id)
    end
end

def create
    @user = User.new(secureUser)
    if @user.valid?
      @user.save
      session[:user_id] = @user.id
      redirect_to events_index_path
    else
      flash[:alert] = @user.errors.full_messages
      redirect_to users_new_path
    end
end

# def destroy
# end

def new
  @logged = logged?
end

# def edit
#   @user = current_user
# end
end
