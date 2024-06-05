# from django.shortcuts import render, get_object_or_404, redirect
# from .forms import ConversationMessageForm
# from .models import Conversation, ConversationMessage
# from products.models import Product
#
#
# def new(request, item_pk):
#     item = get_object_or_404(Product, pk=item_pk)
#     if item.created_by == request.user:
#         return redirect("products:index")
#     conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
#     if conversation:
#         pass
#     if request.method == "POST":
#         form = ConversationMessageForm(request.POST)
#         if form.is_valid():
#             conversation = Conversation.objects.create(item=item)
#             conversation.members.add(request.user)
#             conversation.members.add(item.created_by)
#             conversation.save()
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()
#             return redirect("products:detail", pk=item_pk)
#     else:
#         form = ConversationMessageForm()
#     return render(request, "conversation/new.html", {
#         "form": form})
#
#
# def inbox(request):
#     conversations = Conversation.objects.filter(members__in=[request.user.id])
#
#     return render(request, "conversation/inbox.html", {
#             "conversations": conversations,
#         })
#
#
# def detail(request, pk):
#     conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
#     if request.method == "POST":
#         form = ConversationMessageForm(request.POST)
#         if form.is_valid():
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()
#
#             conversation.save()
#             return redirect("conversation:detail", pk=pk)
#
#     else:
#         form = ConversationMessageForm()
#     return render(request, "conversation/detail.html", {
#         "conversation": conversation,
#         "form": form,
#     })
