class CommentsController < ApplicationController
   protect_from_forgery with: :null_session
   def create
      @comment = Comment.new(secureComment)
      if @comment.valid?
         @comment.save
         redirect_to messages_index_path
      else
         flash[:alert] = @comment.errors.full_messages
         redirect_to messages_index_path
      end
   end
   def destroy    
      message = Message.find_by(id: params[:idMsg])
      comment = Comment.find_by(user: current_user, message: message, id: params[:idCmt] ) #where(user: current_user).where(message: message)
      if comment
         comment.destroy
      else
         flash[:alert] = ['This cannot be removed']
      end
      redirect_to messages_index_path()
   end
end
