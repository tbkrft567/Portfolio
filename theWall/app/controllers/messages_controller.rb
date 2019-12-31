class MessagesController < ApplicationController
   before_action :authorize
   def index
      @messages = Message.all
      @comments = Comment.all
      @user = current_user
   end
   def create
      @message = Message.new(secureMessage)
      if @message.valid?
         @message.save
         redirect_to messages_index_path
      else
         flash[:alert] = @message.errors.full_messages
         redirect_to messages_index_path
      end
   end
end
