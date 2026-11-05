# `board/views.py`

회원·게시글·댓글·신고 — 요청 처리와 응답 연결



[실제 코드 열기](../../../board/views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from functools import wraps

from urllib.parse import urlencode

from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView

from django.core.paginator import Paginator

from django.db.models import Count, F, Q

from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse, reverse_lazy

from django.views.decorators.http import require_POST

from .forms import CommentForm, PostForm, SignupForm

from .matchbot import safe_ensure

from .models import Comment, Post, Report

```

## 함수·클래스 안내

### `member_required` — 25행

로그인하지 않은 사용자는 로그인 화면으로 이동합니다.

입력 이름: `view`

읽을 때 따라갈 호출(중복 제외): `wraps`, `view`, `urlencode`, `redirect`, `request.get_full_path`, `reverse`



### `BoardLogin` — 44행



### `signup` — 51행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `SignupForm`, `render`, `redirect`, `form.is_valid`, `form.save`, `authenticate`, `messages.success`, `login`, `user.get_username`



### `post_list` — 85행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `safe_ensure`, `Post.objects.filter(status=Post.OK).select_related('author__profile').annotate(n_comments=Count('comments', filter=Q(comments__status=Comment.OK))).order_by`, `request.GET.get('q', '').strip`, `request.GET.get`, `Paginator`, `paginator.get_page`, `enumerate`, `request.GET.copy`, `params.pop`, `render`, `Post.objects.filter(status=Post.OK).select_related('author__profile').annotate`, `qs.filter`, `params.urlencode`, `Post.objects.filter(status=Post.OK).select_related`, `Count`, `Q`, `Post.objects.filter`



### `post_detail` — 148행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `request.session.get`, `post.comments.filter(status=Comment.OK).select_related`, `render`, `Post.objects.select_related`, `Post.objects.filter(pk=pk).update`, `post.comments.filter`, `CommentForm`, `Post.objects.filter`, `F`



### `post_create` — 192행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `PostForm`, `render`, `form.is_valid`, `form.save`, `post.save`, `messages.success`, `redirect`



### `post_edit` — 221행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `PostForm`, `render`, `messages.error`, `redirect`, `form.is_valid`, `form.save`, `messages.success`



### `post_delete` — 270행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `messages.error`, `redirect`, `post.delete`, `messages.success`



### `comment_create` — 296행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `CommentForm`, `form.is_valid`, `redirect`, `form.save`, `comment.save`, `messages.success`, `form.errors.values`, `messages.error`, `reverse`



### `comment_delete` — 329행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `redirect`, `comment.delete`, `messages.success`, `messages.error`, `reverse`



### `_report` — 352행

입력 이름: `request`, `obj`, `kw`, `back`

읽을 때 따라갈 호출(중복 제외): `redirect`, `messages.error`, `Report.objects.filter(user=request.user, **kw).exists`, `messages.info`, `Report.objects.create`, `Report.objects.filter(**kw).values('user').distinct().count`, `Report.objects.filter`, `obj.soft_delete`, `messages.success`, `Report.objects.filter(**kw).values('user').distinct`, `request.POST.get`, `Report.objects.filter(**kw).values`



### `post_report` — 400행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `_report`, `reverse`



### `comment_report` — 420행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `_report`, `reverse`

