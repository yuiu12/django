from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['title', 'author']

    # 参与搜索的字段列表
    search_fields = [
        'title', 'content', 'author__username',
        'author__first_name', 'author__last_name'
    ]

    readonly_fields = ['author']
    '''
    list_display 列表页面显示的字段设置
    search_fields 搜索字段的设置
    readonly_fields设置只读字段
    list_filter边栏刷选工具
    list_editable在列表页面可以直接编辑保存的字段，不用进入详情页面就可以修改这些字段内容
    list_per_page列表页面的每页显示记录条数的设置
    ordering用来排序的字段
    fields在表单也缪按显示的字段
    exclude  在表单页面不显示的字段
    fieldsets新增，更改页面的布局进行更多的定制
    empty_value_display自定义字符串空置或None显示的内容
    
    '''
    def save_model(self, request, obj, form, change):
        if not change:  # 如果不是修改，也就是“新建”的时候
            obj.author = request.user
        super(BlogAdmin, self).save_model(request, obj, form, change)
