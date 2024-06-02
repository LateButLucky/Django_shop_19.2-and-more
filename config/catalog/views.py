from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Product, Contact, BlogPost
from .forms import ContactForm, ProductForm


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('home')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_list.html'
    context_object_name = 'blogposts'
    queryset = BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        blogpost = super().get_object(queryset)
        blogpost.views += 1
        blogpost.save()
        return blogpost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_form.html'
    fields = ['title', 'content', 'preview_image', 'published']

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return response


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_form.html'
    fields = ['title', 'content', 'preview_image', 'published']

    def get_success_url(self):
        return reverse_lazy('blog_detail', args=[self.object.slug])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
