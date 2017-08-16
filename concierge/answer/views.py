# from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.views import View

# from .models import Answer
from .forms import AnswerForm


# class AnswerDetail(View):
#     form_class = AnswerForm
#     template_name = 'answer/answer_detail.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             print('Form success!')
#             # return HttpResponseRedirect('/success/')

#         return render(request, self.template_name, {'form': form})


def answer_test(request, form_class=AnswerForm):
    template_name = 'answer/answer_detail.html'
    ctx = {
        'form': form_class()
    }
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            print('success')
            ctx['form'] = form
        else:
            ctx['form'] = form

    return render(request, template_name, ctx)
