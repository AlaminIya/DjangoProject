from django.shortcuts import render, redirect 
from .forms import DweetForm
from django.views.generic.edit import UpdateView, DeleteView
from .models import Dweet, Profile

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    followed_dweets = Dweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
    
    return render(request, "dwitter/dashboard.html", {"form": form, "dweets": followed_dweets},)

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})
# Create your views here.
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile":profile})

def PostEditView(UpdateView):
    model = Post.Dweet 
    fields = ['body']
    template_name = 'dwitter/post_form.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})

