Skip to content 
# Release Notes¶
## Latest Changes¶
### Refactors¶
  * ✅ Simplify tests for `query_params_str_validations`. PR #13218 by @alv2017.
  * ✅ Simplify tests for `app_testing`. PR #13220 by @alv2017.
  * ✅ Simplify tests for `dependency_testing`. PR #13223 by @alv2017.


### Docs¶
  * 🔥 Remove manual type annotations in JWT tutorial to avoid typing expectations (JWT doesn't provide more types). PR #13378 by @tiangolo.
  * 📝 Update docs for Query Params and String Validations, remove obsolete Ellipsis docs (`...`). PR #13377 by @tiangolo.
  * ✏️ Remove duplicate title in docs `body-multiple-params`. PR #13345 by @DanielYang59.
  * 📝 Fix test badge. PR #13313 by @esadek.


### Translations¶
  * 🌐 Update Korean translation for `docs/ko/docs/help-fastapi.md`. PR #13262 by @Zerohertz.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/custom-response.md`. PR #13265 by @11kkw.
  * 🌐 Update Korean translation for `docs/ko/docs/tutorial/security/simple-oauth2.md`. PR #13335 by @yes0ng.
  * 🌐 Add Russian translation for `docs/ru/docs/advanced/response-cookies.md`. PR #13327 by @Stepakinoyan.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/tutorial/static-files.md`. PR #11291 by @ptt3199.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #13257 by @11kkw.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/virtual-environments.md`. PR #13282 by @ptt3199.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/static-files.md`. PR #13285 by @valentinDruzhinin.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/environment-variables.md`. PR #13287 by @ptt3199.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/fastapi-cli.md`. PR #13294 by @ptt3199.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/features.md`. PR #13308 by @valentinDruzhinin.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/learn/index.md`. PR #13306 by @valentinDruzhinin.
  * 🌐 Update Portuguese Translation for `docs/pt/docs/deployment/https.md`. PR #13317 by @Joao-Pedro-P-Holanda.
  * 🌐 Update Portuguese Translation for `docs/pt/docs/index.md`. PR #13328 by @ceb10n.
  * 🌐 Add Russian translation for `docs/ru/docs/advanced/websockets.md`. PR #13279 by @Rishat-F.


### Internal¶
  * ⬆ Bump cloudflare/wrangler-action from 3.13 to 3.14. PR #13350 by @dependabot[bot].
  * ⬆ Bump mkdocs-material from 9.5.18 to 9.6.1. PR #13301 by @dependabot[bot].
  * ⬆ Bump pillow from 11.0.0 to 11.1.0. PR #13300 by @dependabot[bot].
  * 👥 Update FastAPI People - Sponsors. PR #13295 by @tiangolo.
  * 👥 Update FastAPI People - Experts. PR #13303 by @tiangolo.
  * 👥 Update FastAPI GitHub topic repositories. PR #13302 by @tiangolo.
  * 👥 Update FastAPI People - Contributors and Translators. PR #13293 by @tiangolo.
  * ⬆ Bump inline-snapshot from 0.18.1 to 0.19.3. PR #13298 by @dependabot[bot].
  * 🔧 Update sponsors, add Permit. PR #13288 by @tiangolo.


## 0.115.8¶
### Fixes¶
  * 🐛 Fix `OAuth2PasswordRequestForm` and `OAuth2PasswordRequestFormStrict` fixed `grant_type` "password" RegEx. PR #9783 by @skarfie123.


### Refactors¶
  * ✅ Simplify tests for body_multiple_params . PR #13237 by @alejsdev.
  * ♻️ Move duplicated code portion to a static method in the `APIKeyBase` super class. PR #3142 by @ShahriyarR.
  * ✅ Simplify tests for request_files. PR #13182 by @alejsdev.


### Docs¶
  * 📝 Change the word "unwrap" to "unpack" in `docs/en/docs/tutorial/extra-models.md`. PR #13061 by @timothy-jeong.
  * 📝 Update Request Body's `tutorial002` to deal with `tax=0` case. PR #13230 by @togogh.
  * 👥 Update FastAPI People - Experts. PR #13269 by @tiangolo.


### Translations¶
  * 🌐 Add Japanese translation for `docs/ja/docs/environment-variables.md`. PR #13226 by @k94-ishi.
  * 🌐 Add Russian translation for `docs/ru/docs/advanced/async-tests.md`. PR #13227 by @Rishat-F.
  * 🌐 Update Russian translation for `docs/ru/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #13252 by @Rishat-F.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/bigger-applications.md`. PR #13154 by @alv2017.


### Internal¶
  * ⬆️ Add support for Python 3.13. PR #13274 by @tiangolo.
  * ⬆️ Upgrade AnyIO max version for tests, new range: `>=3.2.1,<5.0.0`. PR #13273 by @tiangolo.
  * 🔧 Update Sponsors badges. PR #13271 by @tiangolo.
  * ♻️ Fix `notify_translations.py` empty env var handling for PR label events vs workflow_dispatch. PR #13272 by @tiangolo.
  * ♻️ Refactor and move `scripts/notify_translations.py`, no need for a custom GitHub Action. PR #13270 by @tiangolo.
  * 🔨 Update FastAPI People Experts script, refactor and optimize data fetching to handle rate limits. PR #13267 by @tiangolo.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.12.3 to 1.12.4. PR #13251 by @dependabot[bot].


## 0.115.7¶
### Upgrades¶
  * ⬆️ Upgrade `python-multipart` to >=0.0.18. PR #13219 by @DanielKusyDev.
  * ⬆️ Bump Starlette to allow up to 0.45.0: `>=0.40.0,<0.46.0`. PR #13117 by @Kludex.
  * ⬆️ Upgrade `jinja2` to >=3.1.5. PR #13194 by @DanielKusyDev.


### Refactors¶
  * ✅ Simplify tests for websockets. PR #13202 by @alejsdev.
  * ✅ Simplify tests for request_form_models . PR #13183 by @alejsdev.
  * ✅ Simplify tests for separate_openapi_schemas. PR #13201 by @alejsdev.
  * ✅ Simplify tests for security. PR #13200 by @alejsdev.
  * ✅ Simplify tests for schema_extra_example. PR #13197 by @alejsdev.
  * ✅ Simplify tests for request_model. PR #13195 by @alejsdev.
  * ✅ Simplify tests for request_forms_and_files. PR #13185 by @alejsdev.
  * ✅ Simplify tests for request_forms. PR #13184 by @alejsdev.
  * ✅ Simplify tests for path_query_params. PR #13181 by @alejsdev.
  * ✅ Simplify tests for path_operation_configurations. PR #13180 by @alejsdev.
  * ✅ Simplify tests for header_params. PR #13179 by @alejsdev.
  * ✅ Simplify tests for extra_models. PR #13178 by @alejsdev.
  * ✅ Simplify tests for extra_data_types. PR #13177 by @alejsdev.
  * ✅ Simplify tests for cookie_params. PR #13176 by @alejsdev.
  * ✅ Simplify tests for dependencies. PR #13174 by @alejsdev.
  * ✅ Simplify tests for body_updates. PR #13172 by @alejsdev.
  * ✅ Simplify tests for body_nested_models. PR #13171 by @alejsdev.
  * ✅ Simplify tests for body_multiple_params. PR #13170 by @alejsdev.
  * ✅ Simplify tests for body_fields. PR #13169 by @alejsdev.
  * ✅ Simplify tests for body. PR #13168 by @alejsdev.
  * ✅ Simplify tests for bigger_applications. PR #13167 by @alejsdev.
  * ✅ Simplify tests for background_tasks. PR #13166 by @alejsdev.
  * ✅ Simplify tests for additional_status_codes. PR #13149 by @tiangolo.


### Docs¶
  * ✏️ Update Strawberry integration docs. PR #13155 by @kinuax.
  * 🔥 Remove unused Peewee tutorial files. PR #13158 by @alejsdev.
  * 📝 Update image in body-nested-model docs. PR #11063 by @untilhamza.
  * 📝 Update `fastapi-cli` UI examples in docs. PR #13107 by @Zhongheng-Cheng.
  * 👷 Add new GitHub Action to update contributors, translators, and translation reviewers. PR #13136 by @tiangolo.
  * ✏️ Fix typo in `docs/en/docs/virtual-environments.md`. PR #13124 by @tiangolo.
  * ✏️ Fix error in `docs/en/docs/contributing.md`. PR #12899 by @kingsubin.
  * 📝 Minor corrections in `docs/en/docs/tutorial/sql-databases.md`. PR #13081 by @alv2017.
  * 📝 Update includes in `docs/ru/docs/tutorial/query-param-models.md`. PR #12994 by @alejsdev.
  * ✏️ Fix typo in README installation instructions. PR #13011 by @dave-hay.
  * 📝 Update docs for `fastapi-cli`. PR #13031 by @tiangolo.


### Translations¶
  * 🌐 Update Portuguese Translation for `docs/pt/docs/tutorial/request-forms.md`. PR #13216 by @Joao-Pedro-P-Holanda.
  * 🌐 Update Portuguese translation for `docs/pt/docs/advanced/settings.md`. PR #13209 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/security/oauth2-jwt.md`. PR #13205 by @ceb10n.
  * 🌐 Add Indonesian translation for `docs/id/docs/index.md`. PR #13191 by @gerry-sabar.
  * 🌐 Add Indonesian translation for `docs/id/docs/tutorial/static-files.md`. PR #13092 by @guspan-tanadi.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/security/get-current-user.md`. PR #13188 by @ceb10n.
  * 🌐 Remove Wrong Portuguese translations location for `docs/pt/docs/advanced/benchmarks.md`. PR #13187 by @ceb10n.
  * 🌐 Update Portuguese translations. PR #13156 by @nillvitor.
  * 🌐 Update Russian translation for `docs/ru/docs/tutorial/security/first-steps.md`. PR #13159 by @Yarous.
  * ✏️ Delete unnecessary backspace in `docs/ja/docs/tutorial/path-params-numeric-validations.md`. PR #12238 by @FakeDocument.
  * 🌐 Update Chinese translation for `docs/zh/docs/fastapi-cli.md`. PR #13102 by @Zhongheng-Cheng.
  * 🌐 Add new Spanish translations for all docs with new LLM-assisted system using PydanticAI. PR #13122 by @tiangolo.
  * 🌐 Update existing Spanish translations using the new LLM-assisted system using PydanticAI. PR #13118 by @tiangolo.
  * 🌐 Update Chinese translation for `docs/zh/docs/advanced/security/oauth2-scopes.md`. PR #13110 by @ChenPu2002.
  * 🌐 Add Indonesian translation for `docs/id/docs/tutorial/path-params.md`. PR #13086 by @gerry-sabar.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/sql-databases.md`. PR #13093 by @GeumBinLee.
  * 🌐 Update Chinese translation for `docs/zh/docs/async.md`. PR #13095 by @Zhongheng-Cheng.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/openapi-webhooks.md`. PR #13091 by @Zhongheng-Cheng.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/async-tests.md`. PR #13074 by @Zhongheng-Cheng.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/fastapi-cli.md`. PR #13020 by @ykertytsky.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/events.md`. PR #12512 by @ZhibangYue.
  * 🌐 Add Russian translation for `/docs/ru/docs/tutorial/sql-databases.md`. PR #13079 by @alv2017.
  * 🌐 Update Chinese translation for `docs/zh/docs/advanced/testing-dependencies.md`. PR #13066 by @Zhongheng-Cheng.
  * 🌐 Update Traditional Chinese translation for `docs/zh-hant/docs/tutorial/index.md`. PR #13075 by @codingjenny.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/sql-databases.md`. PR #13051 by @Zhongheng-Cheng.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/query-params-str-validations.md`. PR #12928 by @Vincy1230.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/header-param-models.md`. PR #13040 by @Zhongheng-Cheng.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/path-params.md`. PR #12926 by @Vincy1230.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/first-steps.md`. PR #12923 by @Vincy1230.
  * 🌐 Update Russian translation for `docs/ru/docs/deployment/docker.md`. PR #13048 by @anklav24.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/generate-clients.md`. PR #13030 by @vitumenezes.
  * 🌐 Add Indonesian translation for `docs/id/docs/tutorial/first-steps.md`. PR #13042 by @gerry-sabar.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/cookie-param-models.md`. PR #13038 by @Zhongheng-Cheng.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/request-form-models.md`. PR #13045 by @Zhongheng-Cheng.
  * 🌐 Add Russian translation for `docs/ru/docs/virtual-environments.md`. PR #13026 by @alv2017.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/testing.md`. PR #12968 by @jts8257.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/async-test.md`. PR #12918 by @icehongssii.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/security/oauth2-jwt.md`. PR #10601 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/security/simple-oauth2.md`. PR #10599 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/security/get-current-user.md`. PR #10594 by @AlertRED.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/features.md`. PR #12441 by @codingjenny.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/virtual-environments.md`. PR #12791 by @Vincy1230.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/templates.md`. PR #12726 by @Heumhub.
  * 🌐 Add Russian translation for `docs/ru/docs/fastapi-cli.md`. PR #13041 by @alv2017.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/cookie-param-models.md`. PR #13000 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/header-param-models.md`. PR #13001 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/request-form-models.md`. PR #13002 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/request-forms.md`. PR #13003 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/resources/index.md`. PR #13004 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/how-to/configure-swagger-ui.md`. PR #12898 by @nahyunkeem.
  * 🌐 Add Korean translation to `docs/ko/docs/advanced/additional-status-codes.md`. PR #12715 by @nahyunkeem.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/tutorial/first-steps.md`. PR #12467 by @codingjenny.


### Internal¶
  * 🔧 Add Pydantic 2 trove classifier. PR #13199 by @johnthagen.
  * 👥 Update FastAPI People - Sponsors. PR #13231 by @tiangolo.
  * 👷 Refactor FastAPI People Sponsors to use 2 tokens. PR #13228 by @tiangolo.
  * 👷 Update token for FastAPI People - Sponsors. PR #13225 by @tiangolo.
  * 👷 Add independent CI automation for FastAPI People - Sponsors. PR #13221 by @tiangolo.
  * 👷 Add retries to Smokeshow. PR #13151 by @tiangolo.
  * 🔧 Update Speakeasy sponsor graphic. PR #13147 by @chailandau.
  * 👥 Update FastAPI GitHub topic repositories. PR #13146 by @tiangolo.
  * 👷‍♀️ Add script for GitHub Topic Repositories and update External Links. PR #13135 by @alejsdev.
  * 👥 Update FastAPI People - Contributors and Translators. PR #13145 by @tiangolo.
  * ⬆ Bump markdown-include-variants from 0.0.3 to 0.0.4. PR #13129 by @dependabot[bot].
  * ⬆ Bump inline-snapshot from 0.14.0 to 0.18.1. PR #13132 by @dependabot[bot].
  * ⬆ Bump mkdocs-macros-plugin from 1.0.5 to 1.3.7. PR #13133 by @dependabot[bot].
  * 🔨 Add internal scripts to generate language translations with PydanticAI, include Spanish prompt. PR #13123 by @tiangolo.
  * ⬆ Bump astral-sh/setup-uv from 4 to 5. PR #13096 by @dependabot[bot].
  * 🔧 Update sponsors: rename CryptAPI to BlockBee. PR #13078 by @tiangolo.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.12.2 to 1.12.3. PR #13055 by @dependabot[bot].
  * ⬆ Bump types-ujson from 5.7.0.1 to 5.10.0.20240515. PR #13018 by @dependabot[bot].
  * ⬆ Bump black from 24.3.0 to 24.10.0. PR #13014 by @dependabot[bot].
  * ⬆ Bump inline-snapshot from 0.13.0 to 0.14.0. PR #13017 by @dependabot[bot].
  * ⬆ Bump dirty-equals from 0.6.0 to 0.8.0. PR #13015 by @dependabot[bot].
  * ⬆ Bump cloudflare/wrangler-action from 3.12 to 3.13. PR #12996 by @dependabot[bot].
  * ⬆ Bump astral-sh/setup-uv from 3 to 4. PR #12982 by @dependabot[bot].
  * 🔧 Remove duplicate actions/checkout in `notify-translations.yml`. PR #12915 by @tinyboxvk.
  * 🔧 Update team members. PR #13033 by @tiangolo.
  * 📝 Update sponsors: remove Codacy. PR #13032 by @tiangolo.


## 0.115.6¶
### Fixes¶
  * 🐛 Preserve traceback when an exception is raised in sync dependency with `yield`. PR #5823 by @sombek.


### Refactors¶
  * ♻️ Update tests and internals for compatibility with Pydantic >=2.10. PR #12971 by @tamird.


### Docs¶
  * 📝 Update includes format in docs with an automated script. PR #12950 by @tiangolo.
  * 📝 Update includes for `docs/de/docs/advanced/using-request-directly.md`. PR #12685 by @alissadb.
  * 📝 Update includes for `docs/de/docs/how-to/conditional-openapi.md`. PR #12689 by @alissadb.


### Translations¶
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/async.md`. PR #12990 by @ILoveSorasakiHina.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/tutorial/query-param-models.md`. PR #12932 by @Vincy1230.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/testing-dependencies.md`. PR #12992 by @Limsunoh.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/websockets.md`. PR #12991 by @kwang1215.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/response-model.md`. PR #12933 by @AndreBBM.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/middlewares.md`. PR #12753 by @nahyunkeem.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/openapi-webhooks.md`. PR #12752 by @saeye.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/query-param-models.md`. PR #12931 by @Vincy1230.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/query-param-models.md`. PR #12445 by @gitgernit.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/query-param-models.md`. PR #12940 by @jts8257.
  * 🔥 Remove obsolete tutorial translation to Chinese for `docs/zh/docs/tutorial/sql-databases.md`, it references files that are no longer on the repo. PR #12949 by @tiangolo.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12954 by @pre-commit-ci[bot].


## 0.115.5¶
### Refactors¶
  * ♻️ Update internal checks to support Pydantic 2.10. PR #12914 by @tiangolo.


### Docs¶
  * 📝 Update includes for `docs/en/docs/tutorial/body.md`. PR #12757 by @gsheni.
  * 📝 Update includes in `docs/en/docs/advanced/testing-dependencies.md`. PR #12647 by @AyushSinghal1794.
  * 📝 Update includes for `docs/en/docs/tutorial/metadata.md`. PR #12773 by @Nimitha-jagadeesha.
  * 📝 Update `docs/en/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #12045 by @xuvjso.
  * 📝 Update includes for `docs/en/docs/tutorial/dependencies/global-dependencies.md`. PR #12653 by @vishnuvskvkl.
  * 📝 Update includes for `docs/en/docs/tutorial/body-updates.md`. PR #12712 by @davioc.
  * 📝 Remove mention of Celery in the project generators. PR #12742 by @david-caro.
  * 📝 Update includes in `docs/en/docs/tutorial/header-param-models.md`. PR #12814 by @zhaohan-dong.
  * 📝 Update `contributing.md` docs, include note to not translate this page. PR #12841 by @tiangolo.
  * 📝 Update includes in `docs/en/docs/tutorial/request-forms.md`. PR #12648 by @vishnuvskvkl.
  * 📝 Update includes in `docs/en/docs/tutorial/request-form-models.md`. PR #12649 by @vishnuvskvkl.
  * 📝 Update includes in `docs/en/docs/tutorial/security/oauth2-jwt.md`. PR #12650 by @OCE1960.
  * 📝 Update includes in `docs/vi/docs/tutorial/first-steps.md`. PR #12754 by @MxPy.
  * 📝 Update includes for `docs/pt/docs/advanced/wsgi.md`. PR #12769 by @Nimitha-jagadeesha.
  * 📝 Update includes for `docs/en/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #12815 by @handabaldeep.
  * 📝 Update includes for `docs/en/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #12813 by @handabaldeep.
  * ✏️ Fix error in `docs/en/docs/tutorial/middleware.md`. PR #12819 by @alejsdev.
  * 📝 Update includes for `docs/en/docs/tutorial/security/get-current-user.md`. PR #12645 by @OCE1960.
  * 📝 Update includes for `docs/en/docs/tutorial/security/first-steps.md`. PR #12643 by @OCE1960.
  * 📝 Update includes in `docs/de/docs/advanced/additional-responses.md`. PR #12821 by @zhaohan-dong.
  * 📝 Update includes in `docs/en/docs/advanced/generate-clients.md`. PR #12642 by @AyushSinghal1794.
  * 📝 Fix admonition double quotes with new syntax. PR #12835 by @tiangolo.
  * 📝 Update includes in `docs/zh/docs/advanced/additional-responses.md`. PR #12828 by @zhaohan-dong.
  * 📝 Update includes in `docs/en/docs/tutorial/path-params-numeric-validations.md`. PR #12825 by @zhaohan-dong.
  * 📝 Update includes for `docs/en/docs/advanced/testing-websockets.md`. PR #12761 by @hamidrasti.
  * 📝 Update includes for `docs/en/docs/advanced/using-request-directly.md`. PR #12760 by @hamidrasti.
  * 📝 Update includes for `docs/advanced/wsgi.md`. PR #12758 by @hamidrasti.
  * 📝 Update includes in `docs/de/docs/tutorial/middleware.md`. PR #12729 by @paintdog.
  * 📝 Update includes for `docs/en/docs/tutorial/schema-extra-example.md`. PR #12822 by @tiangolo.
  * 📝 Update includes in `docs/fr/docs/advanced/additional-responses.md`. PR #12634 by @fegmorte.
  * 📝 Update includes in `docs/fr/docs/advanced/path-operation-advanced-configuration.md`. PR #12633 by @kantandane.
  * 📝 Update includes in `docs/fr/docs/advanced/response-directly.md`. PR #12632 by @kantandane.
  * 📝 Update includes for `docs/en/docs/tutorial/header-params.md`. PR #12640 by @vishnuvskvkl.
  * 📝 Update includes in `docs/en/docs/tutorial/cookie-param-models.md`. PR #12639 by @vishnuvskvkl.
  * 📝 Update includes for `docs/en/docs/tutorial/extra-models.md`. PR #12638 by @vishnuvskvkl.
  * 📝 Update includes for `docs/en/docs/tutorial/cors.md`. PR #12637 by @vishnuvskvkl.
  * 📝 Update includes for `docs/en/docs/tutorial/dependencies/sub-dependencies.md`. PR #12810 by @handabaldeep.
  * 📝 Update includes in `docs/en/docs/tutorial/body-nested-models.md`. PR #12812 by @zhaohan-dong.
  * 📝 Update includes in `docs/en/docs/tutorial/path-operation-configuration.md`. PR #12809 by @AlexWendland.
  * 📝 Update includes in `docs/en/docs/tutorial/request-files.md`. PR #12818 by @zhaohan-dong.
  * 📝 Update includes for `docs/en/docs/tutorial/query-param-models.md`. PR #12817 by @handabaldeep.
  * 📝 Update includes in `docs/en/docs/tutorial/path-params.md`. PR #12811 by @AlexWendland.
  * 📝 Update includes in `docs/en/docs/tutorial/response-model.md`. PR #12621 by @kantandane.
  * 📝 Update includes in `docs/en/docs/advanced/websockets.md`. PR #12606 by @vishnuvskvkl.
  * 📝 Updates include for `docs/en/docs/tutorial/cookie-params.md`. PR #12808 by @handabaldeep.
  * 📝 Update includes in `docs/en/docs/tutorial/middleware.md`. PR #12807 by @AlexWendland.
  * 📝 Update includes in `docs/en/docs/advanced/sub-applications.md`. PR #12806 by @zhaohan-dong.
  * 📝 Update includes in `docs/en/docs/advanced/response-headers.md`. PR #12805 by @zhaohan-dong.
  * 📝 Update includes in `docs/fr/docs/tutorial/first-steps.md`. PR #12594 by @kantandane.
  * 📝 Update includes in `docs/en/docs/advanced/response-cookies.md`. PR #12804 by @zhaohan-dong.
  * 📝 Update includes in `docs/en/docs/advanced/path-operation-advanced-configuration.md`. PR #12802 by @zhaohan-dong.
  * 📝 Update includes for `docs/en/docs/advanced/response-directly.md`. PR #12803 by @handabaldeep.
  * 📝 Update includes in `docs/zh/docs/tutorial/background-tasks.md`. PR #12798 by @zhaohan-dong.
  * 📝 Update includes for `docs/de/docs/tutorial/body-multiple-params.md`. PR #12699 by @alissadb.
  * 📝 Update includes in `docs/em/docs/tutorial/body-updates.md`. PR #12799 by @AlexWendland.
  * 📝 Update includes `docs/en/docs/advanced/response-change-status-code.md`. PR #12801 by @handabaldeep.
  * 📝 Update includes `docs/en/docs/advanced/openapi-callbacks.md`. PR #12800 by @handabaldeep.
  * 📝 Update includes in `docs/fr/docs/tutorial/body-multiple-params.md`. PR #12598 by @kantandane.
  * 📝 Update includes in `docs/en/docs/tutorial/body-multiple-params.md`. PR #12593 by @Tashanam-Shahbaz.
  * 📝 Update includes in `docs/pt/docs/tutorial/background-tasks.md`. PR #12736 by @bhunao.
  * 📝 Update includes for `docs/en/docs/advanced/custom-response.md`. PR #12797 by @handabaldeep.
  * 📝 Update includes for `docs/pt/docs/python-types.md`. PR #12671 by @ceb10n.
  * 📝 Update includes for `docs/de/docs/python-types.md`. PR #12660 by @alissadb.
  * 📝 Update includes for `docs/de/docs/advanced/dataclasses.md`. PR #12658 by @alissadb.
  * 📝 Update includes in `docs/fr/docs/tutorial/path-params.md`. PR #12592 by @kantandane.
  * 📝 Update includes for `docs/de/docs/how-to/configure-swagger-ui.md`. PR #12690 by @alissadb.
  * 📝 Update includes in `docs/en/docs/advanced/security/oauth2-scopes.md`. PR #12572 by @krishnamadhavan.
  * 📝 Update includes for `docs/en/docs/how-to/conditional-openapi.md`. PR #12624 by @rabinlamadong.
  * 📝 Update includes in `docs/en/docs/tutorial/dependencies/index.md`. PR #12615 by @bharara.
  * 📝 Update includes in `docs/en/docs/tutorial/response-status-code.md`. PR #12620 by @kantandane.
  * 📝 Update includes in `docs/en/docs/how-to/custom-docs-ui-assets.md`. PR #12623 by @rabinlamadong.
  * 📝 Update includes in `docs/en/docs/advanced/openapi-webhooks.md`. PR #12605 by @salmantec.
  * 📝 Update includes in `docs/en/docs/advanced/events.md`. PR #12604 by @salmantec.
  * 📝 Update includes in `docs/en/docs/advanced/dataclasses.md`. PR #12603 by @salmantec.
  * 📝 Update includes in `docs/es/docs/tutorial/cookie-params.md`. PR #12602 by @antonyare93.
  * 📝 Update includes in `docs/fr/docs/tutorial/path-params-numeric-validations.md`. PR #12601 by @kantandane.
  * 📝 Update includes in `docs/fr/docs/tutorial/background-tasks.md`. PR #12600 by @kantandane.
  * 📝 Update includes in `docs/en/docs/tutorial/encoder.md`. PR #12597 by @tonyjly.
  * 📝 Update includes in `docs/en/docs/how-to/custom-docs-ui-assets.md`. PR #12557 by @philipokiokio.
  * 🎨 Adjust spacing. PR #12635 by @alejsdev.
  * 📝 Update includes in `docs/en/docs/how-to/custom-request-and-route.md`. PR #12560 by @philipokiokio.


### Translations¶
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/testing-websockets.md`. PR #12739 by @Limsunoh.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/environment-variables.md`. PR #12785 by @Vincy1230.
  * 🌐 Add Chinese translation for `docs/zh/docs/environment-variables.md`. PR #12784 by @Vincy1230.
  * 🌐 Add Korean translation for `ko/docs/advanced/response-headers.md`. PR #12740 by @kwang1215.
  * 🌐 Add Chinese translation for `docs/zh/docs/virtual-environments.md`. PR #12790 by @Vincy1230.
  * 🌐 Add Korean translation for `/docs/ko/docs/environment-variables.md`. PR #12526 by @Tolerblanc.
  * 🌐 Add Korean translation for `docs/ko/docs/history-design-future.md`. PR #12646 by @saeye.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/advanced-dependencies.md`. PR #12675 by @kim-sangah.
  * 🌐 Add Korean translation for `docs/ko/docs/how-to/conditional-openapi.md`. PR #12731 by @sptcnl.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/using_request_directly.md`. PR #12738 by @kwang1215.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/testing-events.md`. PR #12741 by @9zimin9.
  * 🌐 Add Korean translation for `docs/ko/docs/security/index.md`. PR #12743 by @kim-sangah.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/path-operation-advanced-configuration.md`. PR #12762 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/wsgi.md`. PR #12659 by @Limsunoh.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/websockets.md`. PR #12703 by @devfernandoa.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/security/simple-oauth2.md`. PR #12520 by @LidiaDomingos.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/response-directly.md`. PR #12674 by @9zimin9.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/middleware.md`. PR #12704 by @devluisrodrigues.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/openapi-callbacks.md`. PR #12705 by @devfernandoa.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/request-files.md`. PR #12706 by @devluisrodrigues.
  * 🌐 Add Portuguese Translation for `docs/pt/docs/advanced/custom-response.md`. PR #12631 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/metadata.md`. PR #12538 by @LinkolnR.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/metadata.md`. PR #12541 by @kwang1215.
  * 🌐 Add Korean Translation for `docs/ko/docs/advanced/response-cookies.md`. PR #12546 by @kim-sangah.
  * 🌐 Add Korean translation for `docs/ko/docs/fastapi-cli.md`. PR #12515 by @dhdld.
  * 🌐 Add Korean Translation for `docs/ko/docs/advanced/response-change-status-code.md`. PR #12547 by @9zimin9.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12907 by @pre-commit-ci[bot].
  * 🔨 Update docs preview script to show previous version and English version. PR #12856 by @tiangolo.
  * ⬆ Bump tiangolo/latest-changes from 0.3.1 to 0.3.2. PR #12794 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.12.0 to 1.12.2. PR #12788 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.11.0 to 1.12.0. PR #12781 by @dependabot[bot].
  * ⬆ Bump cloudflare/wrangler-action from 3.11 to 3.12. PR #12777 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12766 by @pre-commit-ci[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.10.3 to 1.11.0. PR #12721 by @dependabot[bot].
  * ⬆ Update pre-commit requirement from <4.0.0,>=2.17.0 to >=2.17.0,<5.0.0. PR #12749 by @dependabot[bot].
  * ⬆ Bump typer from 0.12.3 to 0.12.5. PR #12748 by @dependabot[bot].
  * ⬆ Update flask requirement from <3.0.0,>=1.1.2 to >=1.1.2,<4.0.0. PR #12747 by @dependabot[bot].
  * ⬆ Bump pillow from 10.4.0 to 11.0.0. PR #12746 by @dependabot[bot].
  * ⬆ Update pytest requirement from <8.0.0,>=7.1.3 to >=7.1.3,<9.0.0. PR #12745 by @dependabot[bot].
  * 🔧 Update sponsors: add Render. PR #12733 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12707 by @pre-commit-ci[bot].


## 0.115.4¶
### Refactors¶
  * ♻️ Update logic to import and check `python-multipart` for compatibility with newer version. PR #12627 by @tiangolo.


### Docs¶
  * 📝 Update includes in `docs/fr/docs/tutorial/body.md`. PR #12596 by @kantandane.
  * 📝 Update includes in `docs/fr/docs/tutorial/debugging.md`. PR #12595 by @kantandane.
  * 📝 Update includes in `docs/fr/docs/tutorial/query-params-str-validations.md`. PR #12591 by @kantandane.
  * 📝 Update includes in `docs/fr/docs/tutorial/query-params.md`. PR #12589 by @kantandane.
  * 📝 Update includes in `docs/en/tutorial/body-fields.md`. PR #12588 by @lucaromagnoli.
  * 📝 Update includes in `docs/de/docs/tutorial/response-status-code.md`. PR #12585 by @abejaranoh.
  * 📝 Update includes in `docs/en/docs/tutorial/body.md`. PR #12586 by @lucaromagnoli.
  * 📝 Update includes in `docs/en/docs/advanced/behind-a-proxy.md`. PR #12583 by @imjuanleonard.
  * 📝 Update includes syntax for `docs/pl/docs/tutorial/first-steps.md`. PR #12584 by @sebkozlo.
  * 📝 Update includes in `docs/en/docs/advanced/middleware.md`. PR #12582 by @montanarograziano.
  * 📝 Update includes in `docs/en/docs/advanced/additional-status-codes.md`. PR #12577 by @krishnamadhavan.
  * 📝 Update includes in `docs/en/docs/advanced/advanced-dependencies.md`. PR #12578 by @krishnamadhavan.
  * 📝 Update includes in `docs/en/docs/advanced/additional-responses.md`. PR #12576 by @krishnamadhavan.
  * 📝 Update includes in `docs/en/docs/tutorial/static-files.md`. PR #12575 by @lucaromagnoli.
  * 📝 Update includes in `docs/en/docs/advanced/async-tests.md`. PR #12568 by @krishnamadhavan.
  * 📝 Update includes in `docs/pt/docs/advanced/behind-a-proxy.md`. PR #12563 by @asmioglou.
  * 📝 Update includes in `docs/de/docs/advanced/security/http-basic-auth.md`. PR #12561 by @Nimitha-jagadeesha.
  * 📝 Update includes in `docs/en/docs/tutorial/background-tasks.md`. PR #12559 by @FarhanAliRaza.
  * 📝 Update includes in `docs/fr/docs/python-types.md`. PR #12558 by @Ismailtlem.
  * 📝 Update includes in `docs/en/docs/how-to/graphql.md`. PR #12564 by @philipokiokio.
  * 📝 Update includes in `docs/en/docs/how-to/extending-openapi.md`. PR #12562 by @philipokiokio.
  * 📝 Update includes for `docs/en/docs/how-to/configure-swagger-ui.md`. PR #12556 by @tiangolo.
  * 📝 Update includes for `docs/en/docs/how-to/separate-openapi-schemas.md`. PR #12555 by @tiangolo.
  * 📝 Update includes for `docs/en/docs/advanced/security/http-basic-auth.md`. PR #12553 by @tiangolo.
  * 📝 Update includes in `docs/en/docs/tutorial/first-steps.md`. PR #12552 by @tiangolo.
  * 📝 Update includes in `docs/en/docs/python-types.md`. PR #12551 by @tiangolo.
  * 📝 Fix link in OAuth2 docs. PR #12550 by @tiangolo.
  * 📝 Add External Link: FastAPI do Zero. PR #12533 by @rennerocha.
  * 📝 Fix minor typos. PR #12516 by @kkirsche.
  * 🌐 Fix rendering issue in translations. PR #12509 by @alejsdev.


### Translations¶
  * 📝 Update includes in `docs/de/docs/advanced/async-tests.md`. PR #12567 by @imjuanleonard.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/sql-databases.md`. PR #12530 by @ilacftemp.
  * 🌐 Add Korean translation for `docs/ko/docs/benchmarks.md`. PR #12540 by @Limsunoh.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/separate-openapi-schemas.md`. PR #12518 by @ilacftemp.
  * 🌐 Update Traditional Chinese translation for `docs/zh-hant/docs/deployment/index.md`. PR #12521 by @codingjenny.
  * 🌐 Update Traditional Chinese translation for `docs/zh-hant/docs/deployment/cloud.md`. PR #12522 by @codingjenny.
  * 🌐 Update Traditional Chinese translation for `docs/zh-hant/docs/how-to/index.md`. PR #12523 by @codingjenny.
  * 🌐 Update Traditional Chinese translation for `docs/zh-hant/docs/tutorial/index.md`. PR #12524 by @codingjenny.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/how-to/index.md`. PR #12468 by @codingjenny.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/tutorial/index.md`. PR #12466 by @codingjenny.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/header-param-models.md`. PR #12437 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/extending-openapi.md`. PR #12470 by @ilacftemp.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/dataclasses.md`. PR #12475 by @leoscarlato.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/custom-request-and-route.md`. PR #12483 by @devfernandoa.


### Internal¶
  * ⬆ Bump cloudflare/wrangler-action from 3.9 to 3.11. PR #12544 by @dependabot[bot].
  * 👷 Update GitHub Action to deploy docs previews to handle missing deploy comments. PR #12527 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12505 by @pre-commit-ci[bot].


## 0.115.3¶
### Upgrades¶
  * ⬆️ Upgrade Starlette to `>=0.40.0,<0.42.0`. PR #12469 by @defnull.


### Docs¶
  * 📝 Fix broken link in docs. PR #12495 by @eltonjncorreia.


### Translations¶
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/fastapi-cli.md`. PR #12444 by @codingjenny.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/deployment/index.md`. PR #12439 by @codingjenny.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/testing-database.md`. PR #12472 by @GuilhermeRameh.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/custom-docs-ui-assets.md`. PR #12473 by @devluisrodrigues.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/response-headers.md`. PR #12458 by @leonardopaloschi.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/deployment/cloud.md`. PR #12440 by @codingjenny.
  * 🌐 Update Portuguese translation for `docs/pt/docs/python-types.md`. PR #12428 by @ceb10n.
  * 🌐 Add Russian translation for `docs/ru/docs/environment-variables.md`. PR #12436 by @wisderfin.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/resources/index.md`. PR #12443 by @codingjenny.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/about/index.md`. PR #12438 by @codingjenny.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/query-param-models.md`. PR #12414 by @ceb10n.
  * 🌐 Remove Portuguese translation for `docs/pt/docs/deployment.md`. PR #12427 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/body-updates.md`. PR #12381 by @andersonrocha0.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/response-cookies.md`. PR #12417 by @Paulofalcao2002.


### Internal¶
  * 👷 Update issue manager workflow . PR #12457 by @alejsdev.
  * 🔧 Update team, include YuriiMotov 🚀. PR #12453 by @tiangolo.
  * 👷 Refactor label-approved, make it an internal script instead of an external GitHub Action. PR #12280 by @tiangolo.
  * 👷 Fix smokeshow, checkout files on CI. PR #12434 by @tiangolo.
  * 👷 Use uv in CI. PR #12281 by @tiangolo.
  * ⬆ Update httpx requirement from <0.25.0,>=0.23.0 to >=0.23.0,<0.28.0. PR #11509 by @dependabot[bot].


## 0.115.2¶
### Upgrades¶
  * ⬆️ Upgrade Starlette to `>=0.37.2,<0.41.0`. PR #12431 by @tiangolo.


## 0.115.1¶
### Fixes¶
  * 🐛 Fix openapi generation with responses kwarg. PR #10895 by @flxdot.
  * 🐛 Remove `Required` shadowing from fastapi using Pydantic v2. PR #12197 by @pachewise.


### Refactors¶
  * ♻️ Update type annotations for improved `python-multipart`. PR #12407 by @tiangolo.


### Docs¶
  * ✨ Add new tutorial for SQL databases with SQLModel. PR #12285 by @tiangolo.
  * 📝 Add External Link: How to profile a FastAPI asynchronous request. PR #12389 by @brouberol.
  * 🔧 Remove `base_path` for `mdx_include` Markdown extension in MkDocs. PR #12391 by @tiangolo.
  * 📝 Update link to Swagger UI configuration docs. PR #12264 by @makisukurisu.
  * 📝 Adding links for Playwright and Vite in `docs/project-generation.md`. PR #12274 by @kayqueGovetri.
  * 📝 Fix small typos in the documentation. PR #12213 by @svlandeg.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/cookie-param-models.md`. PR #12298 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/graphql.md`. PR #12215 by @AnandaCampelo.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/security/oauth2-scopes.md`. PR #12263 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/deployment/concepts.md`. PR #12219 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/conditional-openapi.md`. PR #12221 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/response-directly.md`. PR #12266 by @Joao-Pedro-P-Holanda.
  * 🌐 Update Portuguese translation for `docs/pt/docs/tutorial/cookie-params.md`. PR #12297 by @ceb10n.
  * 🌐 Fix Korean translation for `docs/ko/docs/tutorial/index.md`. PR #12278 by @kkotipy.
  * 🌐 Update Portuguese translation for `docs/pt/docs/advanced/security/http-basic-auth.md`. PR #12275 by @andersonrocha0.
  * 🌐 Add Portuguese translation for `docs/pt/docs/deployment/cloud.md`. PR #12217 by @marcelomarkus.
  * ✏️ Fix typo in `docs/es/docs/python-types.md`. PR #12235 by @JavierSanchezCastro.
  * 🌐 Add Dutch translation for `docs/nl/docs/environment-variables.md`. PR #12200 by @maxscheijen.
  * 🌐 Add Portuguese translation for `docs/pt/docs/deployment/manually.md`. PR #12210 by @JoaoGustavoRogel.
  * 🌐 Add Portuguese translation for `docs/pt/docs/deployment/server-workers.md`. PR #12220 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/configure-swagger-ui.md`. PR #12222 by @marcelomarkus.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12396 by @pre-commit-ci[bot].
  * 🔨 Add script to generate variants of files. PR #12405 by @tiangolo.
  * 🔧 Add speakeasy-api to `sponsors_badge.yml`. PR #12404 by @tiangolo.
  * ➕ Add docs dependency: markdown-include-variants. PR #12399 by @tiangolo.
  * 📝 Fix extra mdx-base-path paths. PR #12397 by @tiangolo.
  * 👷 Tweak labeler to not override custom labels. PR #12398 by @tiangolo.
  * 👷 Update worfkow deploy-docs-notify URL. PR #12392 by @tiangolo.
  * 👷 Update Cloudflare GitHub Action. PR #12387 by @tiangolo.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.10.1 to 1.10.3. PR #12386 by @dependabot[bot].
  * ⬆ Bump mkdocstrings[python] from 0.25.1 to 0.26.1. PR #12371 by @dependabot[bot].
  * ⬆ Bump griffe-typingdoc from 0.2.6 to 0.2.7. PR #12370 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12331 by @pre-commit-ci[bot].
  * 🔧 Update sponsors, remove Fine.dev. PR #12271 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12253 by @pre-commit-ci[bot].
  * ✏️ Fix docstring typos in http security. PR #12223 by @albertvillanova.


## 0.115.0¶
### Highlights¶
Now you can declare `Query`, `Header`, and `Cookie` parameters with Pydantic models. 🎉
#### `Query` Parameter Models¶
Use Pydantic models for `Query` parameters:
```
fromtypingimport Annotated, Literal
fromfastapiimport FastAPI, Query
frompydanticimport BaseModel, Field
app = FastAPI()
classFilterParams(BaseModel):
  limit: int = Field(100, gt=0, le=100)
  offset: int = Field(0, ge=0)
  order_by: Literal["created_at", "updated_at"] = "created_at"
  tags: list[str] = []
@app.get("/items/")
async defread_items(filter_query: Annotated[FilterParams, Query()]):
  return filter_query

```

Read the new docs: Query Parameter Models.
#### `Header` Parameter Models¶
Use Pydantic models for `Header` parameters:
```
fromtypingimport Annotated
fromfastapiimport FastAPI, Header
frompydanticimport BaseModel
app = FastAPI()
classCommonHeaders(BaseModel):
  host: str
  save_data: bool
  if_modified_since: str | None = None
  traceparent: str | None = None
  x_tag: list[str] = []
@app.get("/items/")
async defread_items(headers: Annotated[CommonHeaders, Header()]):
  return headers

```

Read the new docs: Header Parameter Models.
#### `Cookie` Parameter Models¶
Use Pydantic models for `Cookie` parameters:
```
fromtypingimport Annotated
fromfastapiimport Cookie, FastAPI
frompydanticimport BaseModel
app = FastAPI()
classCookies(BaseModel):
  session_id: str
  fatebook_tracker: str | None = None
  googall_tracker: str | None = None
@app.get("/items/")
async defread_items(cookies: Annotated[Cookies, Cookie()]):
  return cookies

```

Read the new docs: Cookie Parameter Models.
#### Forbid Extra Query (Cookie, Header) Parameters¶
Use Pydantic models to restrict extra values for `Query` parameters (also applies to `Header` and `Cookie` parameters).
To achieve it, use Pydantic's `model_config = {"extra": "forbid"}`:
```
fromtypingimport Annotated, Literal
fromfastapiimport FastAPI, Query
frompydanticimport BaseModel, Field
app = FastAPI()
classFilterParams(BaseModel):
  model_config = {"extra": "forbid"}
  limit: int = Field(100, gt=0, le=100)
  offset: int = Field(0, ge=0)
  order_by: Literal["created_at", "updated_at"] = "created_at"
  tags: list[str] = []
@app.get("/items/")
async defread_items(filter_query: Annotated[FilterParams, Query()]):
  return filter_query

```

This applies to `Query`, `Header`, and `Cookie` parameters, read the new docs:
  * Forbid Extra Query Parameters
  * Forbid Extra Headers
  * Forbid Extra Cookies


### Features¶
  * ✨ Add support for Pydantic models for parameters using `Query`, `Cookie`, `Header`. PR #12199 by @tiangolo.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/security/http-basic-auth.md`. PR #12195 by @ceb10n.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12204 by @pre-commit-ci[bot].


## 0.114.2¶
### Fixes¶
  * 🐛 Fix form field regression with `alias`. PR #12194 by @Wurstnase.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/request-form-models.md`. PR #12175 by @ceb10n.
  * 🌐 Add Chinese translation for `docs/zh/docs/project-generation.md`. PR #12170 by @waketzheng.
  * 🌐 Add Dutch translation for `docs/nl/docs/python-types.md`. PR #12158 by @maxscheijen.


### Internal¶
  * 💡 Add comments with instructions for Playwright screenshot scripts. PR #12193 by @tiangolo.
  * ➕ Add inline-snapshot for tests. PR #12189 by @tiangolo.


## 0.114.1¶
### Refactors¶
  * ⚡️ Improve performance in request body parsing with a cache for internal model fields. PR #12184 by @tiangolo.


### Docs¶
  * 📝 Remove duplicate line in docs for `docs/en/docs/environment-variables.md`. PR #12169 by @prometek.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/virtual-environments.md`. PR #12163 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/environment-variables.md`. PR #12162 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/testing.md`. PR #12164 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/debugging.md`. PR #12165 by @marcelomarkus.
  * 🌐 Add Korean translation for `docs/ko/docs/project-generation.md`. PR #12157 by @BORA040126.


### Internal¶
  * ⬆ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR #12173 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12176 by @pre-commit-ci[bot].
  * 👷 Update `issue-manager.yml`. PR #12159 by @tiangolo.
  * ✏️ Fix typo in `fastapi/params.py`. PR #12143 by @surreal30.


## 0.114.0¶
You can restrict form fields to only include those declared in a Pydantic model and forbid any extra field sent in the request using Pydantic's `model_config = {"extra": "forbid"}`:
```
fromtypingimport Annotated
fromfastapiimport FastAPI, Form
frompydanticimport BaseModel
app = FastAPI()
classFormData(BaseModel):
  username: str
  password: str
  model_config = {"extra": "forbid"}
@app.post("/login/")
async deflogin(data: Annotated[FormData, Form()]):
  return data

```

Read the new docs: Form Models - Forbid Extra Form Fields.
### Features¶
  * ✨ Add support for forbidding extra form fields with Pydantic models. PR #12134 by @tiangolo.


### Docs¶
  * 📝 Update docs, Form Models section title, to match config name. PR #12152 by @tiangolo.


### Internal¶
  * ✅ Update internal tests for latest Pydantic, including CI tweaks to install the latest Pydantic. PR #12147 by @tiangolo.


## 0.113.0¶
Now you can declare form fields with Pydantic models:
```
fromtypingimport Annotated
fromfastapiimport FastAPI, Form
frompydanticimport BaseModel
app = FastAPI()
classFormData(BaseModel):
  username: str
  password: str
@app.post("/login/")
async deflogin(data: Annotated[FormData, Form()]):
  return data

```

Read the new docs: Form Models.
### Features¶
  * ✨ Add support for Pydantic models in `Form` parameters. PR #12129 by @tiangolo.


### Internal¶
  * 🔧 Update sponsors: Coherence link. PR #12130 by @tiangolo.


## 0.112.4¶
This release is mainly a big internal refactor to enable adding support for Pydantic models for `Form` fields, but that feature comes in the next release.
This release shouldn't affect apps using FastAPI in any way. You don't even have to upgrade to this version yet. It's just a checkpoint. 🤓
### Refactors¶
  * ♻️ Refactor deciding if `embed` body fields, do not overwrite fields, compute once per router, refactor internals in preparation for Pydantic models in `Form`, `Query` and others. PR #12117 by @tiangolo.


### Internal¶
  * ⏪️ Temporarily revert "✨ Add support for Pydantic models in `Form` parameters" to make a checkpoint release. PR #12128 by @tiangolo. Restored by PR #12129.
  * ✨ Add support for Pydantic models in `Form` parameters. PR #12127 by @tiangolo. Reverted by PR #12128 to make a checkpoint release with only refactors. Restored by PR #12129.


## 0.112.3¶
This release is mainly internal refactors, it shouldn't affect apps using FastAPI in any way. You don't even have to upgrade to this version yet. There are a few bigger releases coming right after. 🚀
### Refactors¶
  * ♻️ Refactor internal `check_file_field()`, rename to `ensure_multipart_is_installed()` to clarify its purpose. PR #12106 by @tiangolo.
  * ♻️ Rename internal `create_response_field()` to `create_model_field()` as it's used for more than response models. PR #12103 by @tiangolo.
  * ♻️ Refactor and simplify internal data from `solve_dependencies()` using dataclasses. PR #12100 by @tiangolo.
  * ♻️ Refactor and simplify internal `analyze_param()` to structure data with dataclasses instead of tuple. PR #12099 by @tiangolo.
  * ♻️ Refactor and simplify dependencies data structures with dataclasses. PR #12098 by @tiangolo.


### Docs¶
  * 📝 Add External Link: Techniques and applications of SQLAlchemy global filters in FastAPI. PR #12109 by @TheShubhendra.
  * 📝 Add note about `time.perf_counter()` in middlewares. PR #12095 by @tiangolo.
  * 📝 Tweak middleware code sample `time.time()` to `time.perf_counter()`. PR #11957 by @domdent.
  * 🔧 Update sponsors: Coherence. PR #12093 by @tiangolo.
  * 📝 Fix async test example not to trigger DeprecationWarning. PR #12084 by @marcinsulikowski.
  * 📝 Update `docs_src/path_params_numeric_validations/tutorial006.py`. PR #11478 by @MuhammadAshiqAmeer.
  * 📝 Update comma in `docs/en/docs/async.md`. PR #12062 by @Alec-Gillis.
  * 📝 Update docs about serving FastAPI: ASGI servers, Docker containers, etc.. PR #12069 by @tiangolo.
  * 📝 Clarify `response_class` parameter, validations, and returning a response directly. PR #12067 by @tiangolo.
  * 📝 Fix minor typos and issues in the documentation. PR #12063 by @svlandeg.
  * 📝 Add note in Docker docs about ensuring graceful shutdowns and lifespan events with `CMD` exec form. PR #11960 by @GPla.


### Translations¶
  * 🌐 Add Dutch translation for `docs/nl/docs/features.md`. PR #12101 by @maxscheijen.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/testing-events.md`. PR #12108 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/security/index.md`. PR #12114 by @ceb10n.
  * 🌐 Add Dutch translation for `docs/nl/docs/index.md`. PR #12042 by @svlandeg.
  * 🌐 Update Chinese translation for `docs/zh/docs/how-to/index.md`. PR #12070 by @synthpop123.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12115 by @pre-commit-ci[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.10.0 to 1.10.1. PR #12120 by @dependabot[bot].
  * ⬆ Bump pillow from 10.3.0 to 10.4.0. PR #12105 by @dependabot[bot].
  * 💚 Set `include-hidden-files` to `True` when using the `upload-artifact` GH action. PR #12118 by @svlandeg.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.0. PR #12112 by @dependabot[bot].
  * 🔧 Update sponsors link: Coherence. PR #12097 by @tiangolo.
  * 🔧 Update labeler config to handle sponsorships data. PR #12096 by @tiangolo.
  * 🔧 Update sponsors, remove Kong. PR #12085 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12076 by @pre-commit-ci[bot].
  * 👷 Update `latest-changes` GitHub Action. PR #12073 by @tiangolo.


## 0.112.2¶
### Fixes¶
  * 🐛 Fix `allow_inf_nan` option for Param and Body classes. PR #11867 by @giunio-prc.
  * 🐛 Ensure that `app.include_router` merges nested lifespans. PR #9630 by @Lancetnik.


### Refactors¶
  * 🎨 Fix typing annotation for semi-internal `FastAPI.add_api_route()`. PR #10240 by @ordinary-jamie.
  * ⬆️ Upgrade version of Ruff and reformat. PR #12032 by @tiangolo.


### Docs¶
  * 📝 Fix a typo in `docs/en/docs/virtual-environments.md`. PR #12064 by @aymenkrifa.
  * 📝 Add docs about Environment Variables and Virtual Environments. PR #12054 by @tiangolo.
  * 📝 Add Asyncer mention in async docs. PR #12037 by @tiangolo.
  * 📝 Move the Features docs to the top level to improve the main page menu. PR #12036 by @tiangolo.
  * ✏️ Fix import typo in reference example for `Security`. PR #11168 by @0shah0.
  * 📝 Highlight correct line in tutorial `docs/en/docs/tutorial/body-multiple-params.md`. PR #11978 by @svlandeg.
  * 🔥 Remove Sentry link from Advanced Middleware docs. PR #12031 by @alejsdev.
  * 📝 Clarify management tasks for translations, multiples files in one PR. PR #12030 by @tiangolo.
  * 📝 Edit the link to the OpenAPI "Responses Object" and "Response Object" sections in the "Additional Responses in OpenAPI" section. PR #11996 by @VaitoSoi.
  * 🔨 Specify `email-validator` dependency with dash. PR #11515 by @jirikuncar.
  * 🌐 Add Spanish translation for `docs/es/docs/project-generation.md`. PR #11947 by @alejsdev.
  * 📝 Fix minor typo. PR #12026 by @MicaelJarniac.
  * 📝 Several docs improvements, tweaks, and clarifications. PR #11390 by @nilslindemann.
  * 📝 Add missing `compresslevel` parameter on docs for `GZipMiddleware`. PR #11350 by @junah201.
  * 📝 Fix inconsistent response code when item already exists in docs for testing. PR #11818 by @lokomilo.
  * 📝 Update `docs/en/docs/tutorial/body.md` with Python 3.10 union type example. PR #11415 by @rangzen.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/request_file.md`. PR #12018 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Japanese translation for `docs/ja/docs/learn/index.md`. PR #11592 by @ukwhatn.
  * 📝 Update Spanish translation docs for consistency. PR #12044 by @alejsdev.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #12028 by @xuvjso.
  * 📝 Update FastAPI People, do not translate to have the most recent info. PR #12034 by @tiangolo.
  * 🌐 Update Urdu translation for `docs/ur/docs/benchmarks.md`. PR #10046 by @AhsanSheraz.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #12046 by @pre-commit-ci[bot].
  * 🔧 Update coverage config files. PR #12035 by @tiangolo.
  * 🔨 Standardize shebang across shell scripts. PR #11942 by @gitworkflows.
  * ⬆ Update sqlalchemy requirement from <1.4.43,>=1.3.18 to >=1.3.18,<2.0.33. PR #11979 by @dependabot[bot].
  * 🔊 Remove old ignore warnings. PR #11950 by @tiangolo.
  * ⬆️ Upgrade griffe-typingdoc for the docs. PR #12029 by @tiangolo.
  * 🙈 Add .coverage* to `.gitignore`. PR #11940 by @gitworkflows.
  * ⚙️ Record and show test coverage contexts (what test covers which line). PR #11518 by @slafs.


## 0.112.1¶
### Upgrades¶
  * ⬆️ Allow Starlette 0.38.x, update the pin to `>=0.37.2,<0.39.0`. PR #11876 by @musicinmybrain.


### Docs¶
  * 📝 Update docs section about "Don't Translate these Pages". PR #12022 by @tiangolo.
  * 📝 Add documentation for non-translated pages and scripts to verify them. PR #12020 by @tiangolo.
  * 📝 Update docs about discussions questions. PR #11985 by @tiangolo.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/bigger-applications.md`. PR #11971 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/testing-websockets.md`. PR #11994 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/testing-dependencies.md`. PR #11995 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/using-request-directly.md`. PR #11956 by @ceb10n.
  * 🌐 Add French translation for `docs/fr/docs/tutorial/body-multiple-params.md`. PR #11796 by @pe-brian.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/query-params.md`. PR #11557 by @caomingpei.
  * 🌐 Update typo in Chinese translation for `docs/zh/docs/advanced/testing-dependencies.md`. PR #11944 by @bestony.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/sub-applications.md` and `docs/pt/docs/advanced/behind-a-proxy.md`. PR #11856 by @marcelomarkus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/cors.md` and `docs/pt/docs/tutorial/middleware.md`. PR #11916 by @wesinalves.
  * 🌐 Add French translation for `docs/fr/docs/tutorial/path-params-numeric-validations.md`. PR #11788 by @pe-brian.


### Internal¶
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0. PR #11727 by @dependabot[bot].
  * 🔧 Add changelog URL to `pyproject.toml`, shows in PyPI. PR #11152 by @Pierre-VF.
  * 👷 Do not sync labels as it overrides manually added labels. PR #12024 by @tiangolo.
  * 👷🏻 Update Labeler GitHub Actions. PR #12019 by @tiangolo.
  * 🔧 Update configs for MkDocs for languages and social cards. PR #12016 by @tiangolo.
  * 👷 Update permissions and config for labeler GitHub Action. PR #12008 by @tiangolo.
  * 👷🏻 Add GitHub Action label-checker. PR #12005 by @tiangolo.
  * 👷 Add label checker GitHub Action. PR #12004 by @tiangolo.
  * 👷 Update GitHub Action add-to-project. PR #12002 by @tiangolo.
  * 🔧 Update labeler GitHub Action. PR #12001 by @tiangolo.
  * 👷 Add GitHub Action labeler. PR #12000 by @tiangolo.
  * 👷 Add GitHub Action add-to-project. PR #11999 by @tiangolo.
  * 📝 Update admonitions in docs missing. PR #11998 by @tiangolo.
  * 🔨 Update docs.py script to enable dirty reload conditionally. PR #11986 by @tiangolo.
  * 🔧 Update MkDocs instant previews. PR #11982 by @tiangolo.
  * 🐛 Fix deploy docs previews script to handle mkdocs.yml files. PR #11984 by @tiangolo.
  * 💡 Add comment about custom Termynal line-height. PR #11976 by @tiangolo.
  * 👷 Add alls-green for test-redistribute. PR #11974 by @tiangolo.
  * 👷 Update docs-previews to handle no docs changes. PR #11975 by @tiangolo.
  * 🔨 Refactor script `deploy_docs_status.py` to account for deploy URLs with or without trailing slash. PR #11965 by @tiangolo.
  * 🔒️ Update permissions for deploy-docs action. PR #11964 by @tiangolo.
  * 👷🏻 Add deploy docs status and preview links to PRs. PR #11961 by @tiangolo.
  * 🔧 Update docs setup with latest configs and plugins. PR #11953 by @tiangolo.
  * 🔇 Ignore warning from attrs in Trio. PR #11949 by @tiangolo.


## 0.112.0¶
### Breaking Changes¶
  * ♻️ Add support for `pip install "fastapi[standard]"` with standard dependencies and `python -m fastapi`. PR #11935 by @tiangolo.


#### Summary¶
Install with:
```
pipinstall"fastapi[standard]"

```

#### Other Changes¶
  * This adds support for calling the CLI as:


```
python-mfastapi

```

  * And it upgrades `fastapi-cli[standard] >=0.0.5`.


#### Technical Details¶
Before this, `fastapi` would include the standard dependencies, with Uvicorn and the `fastapi-cli`, etc.
And `fastapi-slim` would not include those standard dependencies.
Now `fastapi` doesn't include those standard dependencies unless you install with `pip install "fastapi[standard]"`.
Before, you would install `pip install fastapi`, now you should include the `standard` optional dependencies (unless you want to exclude one of those): `pip install "fastapi[standard]"`.
This change is because having the standard optional dependencies installed by default was being inconvenient to several users, and having to install instead `fastapi-slim` was not being a feasible solution.
Discussed here: #11522 and here: #11525
### Docs¶
  * ✏️ Fix typos in docs. PR #11926 by @jianghuyiyuan.
  * 📝 Tweak management docs. PR #11918 by @tiangolo.
  * 🚚 Rename GitHub links from tiangolo/fastapi to fastapi/fastapi. PR #11913 by @tiangolo.
  * 📝 Add docs about FastAPI team and project management. PR #11908 by @tiangolo.
  * 📝 Re-structure docs main menu. PR #11904 by @tiangolo.
  * 📝 Update Speakeasy URL. PR #11871 by @ndimares.


### Translations¶
  * 🌐 Update Portuguese translation for `docs/pt/docs/alternatives.md`. PR #11931 by @ceb10n.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/sub-dependencies.md`. PR #10515 by @AlertRED.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/response-change-status-code.md`. PR #11863 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/reference/background.md`. PR #11849 by @lucasbalieiro.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #11848 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/reference/apirouter.md`. PR #11843 by @lucasbalieiro.


### Internal¶
  * 🔧 Update sponsors: add liblab. PR #11934 by @tiangolo.
  * 👷 Update GitHub Action label-approved permissions. PR #11933 by @tiangolo.
  * 👷 Refactor GitHub Action to comment docs deployment URLs and update token. PR #11925 by @tiangolo.
  * 👷 Update tokens for GitHub Actions. PR #11924 by @tiangolo.
  * 👷 Update token permissions to comment deployment URL in docs. PR #11917 by @tiangolo.
  * 👷 Update token permissions for GitHub Actions. PR #11915 by @tiangolo.
  * 👷 Update GitHub Actions token usage. PR #11914 by @tiangolo.
  * 👷 Update GitHub Action to notify translations with label `approved-1`. PR #11907 by @tiangolo.
  * 🔧 Update sponsors, remove Reflex. PR #11875 by @tiangolo.
  * 🔧 Update sponsors: remove TalkPython. PR #11861 by @tiangolo.
  * 🔨 Update docs Termynal scripts to not include line nums for local dev. PR #11854 by @tiangolo.


## 0.111.1¶
### Upgrades¶
  * ➖ Remove `orjson` and `ujson` from default dependencies. PR #11842 by @tiangolo.
    * These dependencies are still installed when you install with `pip install "fastapi[all]"`. But they are not included in `pip install fastapi`.
  * 📝 Restored Swagger-UI links to use the latest version possible. PR #11459 by @UltimateLobster.


### Docs¶
  * ✏️ Rewording in `docs/en/docs/fastapi-cli.md`. PR #11716 by @alejsdev.
  * 📝 Update Hypercorn links in all the docs. PR #11744 by @kittydoor.
  * 📝 Update docs with Ariadne reference from Starlette to FastAPI. PR #11797 by @DamianCzajkowski.
  * 📝 Update fastapi instrumentation external link. PR #11317 by @softwarebloat.
  * ✏️ Fix links to alembic example repo in docs. PR #11628 by @augiwan.
  * ✏️ Update `docs/en/docs/fastapi-cli.md`. PR #11715 by @alejsdev.
  * 📝 Update External Links . PR #11500 by @devon2018.
  * 📝 Add External Link: Tutorial de FastAPI, ¿el mejor framework de Python?. PR #11618 by @EduardoZepeda.
  * 📝 Fix typo in `docs/en/docs/tutorial/body-multiple-params.md`. PR #11698 by @mwb-u.
  * 📝 Add External Link: Deploy a Serverless FastAPI App with Neon Postgres and AWS App Runner at any scale. PR #11633 by @ananis25.
  * 📝 Update `security/first-steps.md`. PR #11674 by @alejsdev.
  * 📝 Update `security/first-steps.md`. PR #11673 by @alejsdev.
  * 📝 Update note in `path-params-numeric-validations.md`. PR #11672 by @alejsdev.
  * 📝 Tweak intro docs about `Annotated` and `Query()` params. PR #11664 by @tiangolo.
  * 📝 Update JWT auth documentation to use PyJWT instead of pyhon-jose. PR #11589 by @estebanx64.
  * 📝 Update docs. PR #11603 by @alejsdev.
  * ✏️ Fix typo: convert every 're-use' to 'reuse'.. PR #11598 by @hasansezertasan.
  * ✏️ Fix typo in `fastapi/applications.py`. PR #11593 by @petarmaric.
  * ✏️ Fix link in `fastapi-cli.md`. PR #11524 by @svlandeg.


### Translations¶
  * 🌐 Add Spanish translation for `docs/es/docs/how-to/graphql.md`. PR #11697 by @camigomezdev.
  * 🌐 Add Portuguese translation for `docs/pt/docs/reference/index.md`. PR #11840 by @lucasbalieiro.
  * 🌐 Fix link in German translation. PR #11836 by @anitahammer.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/sub-dependencies.md`. PR #11792 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Turkish translation for `docs/tr/docs/tutorial/request-forms.md`. PR #11553 by @hasansezertasan.
  * 🌐 Add Portuguese translation for `docs/pt/docs/reference/exceptions.md`. PR #11834 by @lucasbalieiro.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/global-dependencies.md`. PR #11826 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/general.md`. PR #11825 by @lucasbalieiro.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/async-tests.md`. PR #11808 by @ceb10n.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/first-steps.md`. PR #11809 by @vkhoroshchak.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/dependencies-in-path-operation-operators.md`. PR #11804 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Chinese translation for `docs/zh/docs/fastapi-cli.md`. PR #11786 by @logan2d5.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/openapi-webhooks.md`. PR #11791 by @ceb10n.
  * 🌐 Update Chinese translation for `docs/tutorial/security/oauth2-jwt.md`. PR #11781 by @logan2d5.
  * 📝 Fix image missing in French translation for `docs/fr/docs/async.md` . PR #11787 by @pe-brian.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/advanced-dependencies.md`. PR #11775 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #11768 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/additional-status-codes.md`. PR #11753 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/dependencies/index.md`. PR #11757 by @Joao-Pedro-P-Holanda.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/settings.md`. PR #11739 by @Joao-Pedro-P-Holanda.
  * 🌐 Add French translation for `docs/fr/docs/learn/index.md`. PR #11712 by @benjaminvandammeholberton.
  * 🌐 Add Portuguese translation for `docs/pt/docs/how-to/index.md`. PR #11731 by @vhsenna.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/additional-responses.md`. PR #11736 by @ceb10n.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/benchmarks.md`. PR #11713 by @ceb10n.
  * 🌐 Fix Korean translation for `docs/ko/docs/tutorial/response-status-code.md`. PR #11718 by @nayeonkinn.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/extra-data-types.md`. PR #11711 by @nayeonkinn.
  * 🌐 Fix Korean translation for `docs/ko/docs/tutorial/body-nested-models.md`. PR #11710 by @nayeonkinn.
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/fastapi-cli.md`. PR #11641 by @ayr-ton.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/fastapi-people.md`. PR #11639 by @hsuanchi.
  * 🌐 Add Turkish translation for `docs/tr/docs/advanced/index.md`. PR #11606 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/deployment/cloud.md`. PR #11610 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/advanced/security/index.md`. PR #11609 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/advanced/testing-websockets.md`. PR #11608 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/how-to/general.md`. PR #11607 by @hasansezertasan.
  * 🌐 Update Chinese translation for `docs/zh/docs/advanced/templates.md`. PR #11620 by @chaoless.
  * 🌐 Add Turkish translation for `docs/tr/docs/deployment/index.md`. PR #11605 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/tutorial/static-files.md`. PR #11599 by @hasansezertasan.
  * 🌐 Polish translation for `docs/pl/docs/fastapi-people.md`. PR #10196 by @isulim.
  * 🌐 Add Turkish translation for `docs/tr/docs/advanced/wsgi.md`. PR #11575 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/tutorial/cookie-params.md`. PR #11561 by @hasansezertasan.
  * 🌐 Add Russian translation for `docs/ru/docs/about/index.md`. PR #10961 by @s111d.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/sql-databases.md`. PR #11539 by @chaoless.
  * 🌐 Add Chinese translation for `docs/zh/docs/how-to/configure-swagger-ui.md`. PR #11501 by @Lucas-lyh.
  * 🌐 Update Chinese translation for `/docs/advanced/security/http-basic-auth.md`. PR #11512 by @nick-cjyx9.


### Internal¶
  * ♻️ Simplify internal docs script. PR #11777 by @gitworkflows.
  * 🔧 Update sponsors: add Fine. PR #11784 by @tiangolo.
  * 🔧 Tweak sponsors: Kong URL. PR #11765 by @tiangolo.
  * 🔧 Tweak sponsors: Kong URL. PR #11764 by @tiangolo.
  * 🔧 Update sponsors, add Stainless. PR #11763 by @tiangolo.
  * 🔧 Update sponsors, add Zuplo. PR #11729 by @tiangolo.
  * 🔧 Update Sponsor link: Coherence. PR #11730 by @tiangolo.
  * 👥 Update FastAPI People. PR #11669 by @tiangolo.
  * 🔧 Add sponsor Kong. PR #11662 by @tiangolo.
  * 👷 Update Smokeshow, fix sync download artifact and smokeshow configs. PR #11563 by @tiangolo.
  * 👷 Update Smokeshow download artifact GitHub Action. PR #11562 by @tiangolo.
  * 👷 Update GitHub actions to download and upload artifacts to v4, for docs and coverage. PR #11550 by @tamird.
  * 👷 Tweak CI for test-redistribute, add needed env vars for slim. PR #11549 by @tiangolo.
  * 👥 Update FastAPI People. PR #11511 by @tiangolo.


## 0.111.0¶
### Features¶
  * ✨ Add FastAPI CLI, the new `fastapi` command. PR #11522 by @tiangolo.
    * New docs: FastAPI CLI.


Try it out with:
```
$ pipinstall--upgradefastapi
$ fastapidevmain.py
 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                           │
 │ Serving at: http://127.0.0.1:8000         │
 │                           │
 │ API docs: http://127.0.0.1:8000/docs        │
 │                           │
 │ Running in development mode, for production use:  │
 │                           │
 │ fastapi run                    │
 │                           │
 ╰─────────────────────────────────────────────────────╯
INFO:   Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:   Started reloader process [2248755] using WatchFiles
INFO:   Started server process [2248757]
INFO:   Waiting for application startup.
INFO:   Application startup complete.

```

### Refactors¶
  * 🔧 Add configs and setup for `fastapi-slim` including optional extras `fastapi-slim[standard]`, and `fastapi` including by default the same `standard` extras. PR #11503 by @tiangolo.


## 0.110.3¶
### Docs¶
  * 📝 Update references to Python version, FastAPI supports all the current versions, no need to make the version explicit. PR #11496 by @tiangolo.
  * ✏️ Fix typo in `fastapi/security/api_key.py`. PR #11481 by @ch33zer.
  * ✏️ Fix typo in `security/http.py`. PR #11455 by @omarmoo5.


### Translations¶
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/benchmarks.md`. PR #11484 by @KNChiu.
  * 🌐 Update Chinese translation for `docs/zh/docs/fastapi-people.md`. PR #11476 by @billzhong.
  * 🌐 Add Chinese translation for `docs/zh/docs/how-to/index.md` and `docs/zh/docs/how-to/general.md`. PR #11443 by @billzhong.
  * 🌐 Add Spanish translation for cookie-params `docs/es/docs/tutorial/cookie-params.md`. PR #11410 by @fabianfalon.


### Internal¶
  * ⬆ Bump mkdocstrings[python] from 0.23.0 to 0.24.3. PR #11469 by @dependabot[bot].
  * 🔨 Update internal scripts and remove unused ones. PR #11499 by @tiangolo.
  * 🔧 Migrate from Hatch to PDM for the internal build. PR #11498 by @tiangolo.
  * ⬆️ Upgrade MkDocs Material and re-enable cards. PR #11466 by @tiangolo.
  * ⬆ Bump pillow from 10.2.0 to 10.3.0. PR #11403 by @dependabot[bot].
  * 🔧 Ungroup dependabot updates. PR #11465 by @tiangolo.


## 0.110.2¶
### Fixes¶
  * 🐛 Fix support for query parameters with list types, handle JSON encoding Pydantic `UndefinedType`. PR #9929 by @arjwilliams.


### Refactors¶
  * ♻️ Simplify Pydantic configs in OpenAPI models in `fastapi/openapi/models.py`. PR #10886 by @JoeTanto2.
  * ✨ Add support for Pydantic's 2.7 new deprecated Field parameter, remove URL from validation errors response. PR #11461 by @tiangolo.


### Docs¶
  * 📝 Fix types in examples under `docs_src/extra_data_types`. PR #10535 by @nilslindemann.
  * 📝 Update references to UJSON. PR #11464 by @tiangolo.
  * 📝 Tweak docs and translations links, typos, format. PR #11389 by @nilslindemann.
  * 📝 Fix typo in `docs/es/docs/async.md`. PR #11400 by @fabianfalon.
  * 📝 Update OpenAPI client generation docs to use `@hey-api/openapi-ts`. PR #11339 by @jordanshatford.


### Translations¶
  * 🌐 Update Chinese translation for `docs/zh/docs/index.html`. PR #11430 by @waketzheng.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #11411 by @anton2yakovlev.
  * 🌐 Add Portuguese translations for `learn/index.md` `resources/index.md` `help/index.md` `about/index.md`. PR #10807 by @nazarepiedady.
  * 🌐 Update Russian translations for deployments docs. PR #11271 by @Lufa1u.
  * 🌐 Add Bengali translations for `docs/bn/docs/python-types.md`. PR #11376 by @imtiaz101325.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/security/simple-oauth2.md`. PR #5744 by @KdHyeon0661.
  * 🌐 Add Korean translation for `docs/ko/docs/help-fastapi.md`. PR #4139 by @kty4119.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/events.md`. PR #5087 by @pers0n4.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/path-operation-configuration.md`. PR #1954 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/request-forms-and-files.md`. PR #1946 by @SwftAlpc.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #10532 by @AlertRED.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/debugging.md`. PR #5695 by @JungWooGeon.


### Internal¶
  * ⬆️ Upgrade version of typer for docs. PR #11393 by @tiangolo.


## 0.110.1¶
### Fixes¶
  * 🐛 Fix parameterless `Depends()` with generics. PR #9479 by @nzig.


### Refactors¶
  * ♻️ Update mypy. PR #11049 by @k0t3n.
  * ♻️ Simplify string format with f-strings in `fastapi/applications.py`. PR #11335 by @igeni.


### Upgrades¶
  * ⬆️ Upgrade Starlette to >=0.37.2,<0.38.0, remove Starlette filterwarning for internal tests. PR #11266 by @nothielf.


### Docs¶
  * 📝 Tweak docs and translations links and remove old docs translations. PR #11381 by @tiangolo.
  * ✏️ Fix typo in `fastapi/security/oauth2.py`. PR #11368 by @shandongbinzhou.
  * 📝 Update links to Pydantic docs to point to new website. PR #11328 by @alejsdev.
  * ✏️ Fix typo in `docs/en/docs/tutorial/extra-models.md`. PR #11329 by @alejsdev.
  * 📝 Update `project-generation.md`. PR #11326 by @alejsdev.
  * 📝 Update External Links. PR #11327 by @alejsdev.
  * 🔥 Remove link to Pydantic's benchmark, on other i18n pages.. PR #11224 by @hirotoKirimaru.
  * ✏️ Fix typos in docstrings. PR #11295 by @davidhuser.
  * 🛠️ Improve Node.js script in docs to generate TypeScript clients. PR #11293 by @alejsdev.
  * 📝 Update examples for tests to replace "inexistent" for "nonexistent". PR #11220 by @Homesteady.
  * 📝 Update `python-multipart` GitHub link in all docs from `https://andrew-d.github.io/python-multipart/` to `https://github.com/Kludex/python-multipart`. PR #11239 by @joshjhans.


### Translations¶
  * 🌐 Add German translation for `docs/de/docs/tutorial/response-status-code.md`. PR #10357 by @nilslindemann.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/query-params.md`. PR #3480 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/body.md`. PR #3481 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/path-params.md`. PR #3479 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/tutorial/body-fields.md`. PR #3496 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/tutorial/extra-models.md`. PR #3497 by @jaystone776.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/metadata.md`. PR #2667 by @tokusumi.
  * 🌐 Add German translation for `docs/de/docs/contributing.md`. PR #10487 by @nilslindemann.
  * 🌐 Update Japanese translation of `docs/ja/docs/tutorial/query-params.md`. PR #10808 by @urushio.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/security/get-current-user.md`. PR #3842 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/openapi-callbacks.md`. PR #3825 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/extending-openapi.md`. PR #3823 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/testing-dependencies.md`. PR #3819 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/custom-request-and-route.md`. PR #3816 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/external-links.md`. PR #3833 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/templates.md`. PR #3812 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/sub-applications.md`. PR #3811 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/async-sql-databases.md`. PR #3805 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/middleware.md`. PR #3804 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/dataclasses.md`. PR #3803 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/using-request-directly.md`. PR #3802 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/security/http-basic-auth.md`. PR #3801 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/security/oauth2-scopes.md`. PR #3800 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/cookie-params.md`. PR #3486 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/header-params.md`. PR #3487 by @jaystone776.
  * 🌐 Update Chinese translation for `docs/tutorial/response-status-code.md`. PR #3498 by @jaystone776.
  * 🌐 Add German translation for `docs/de/docs/tutorial/security/first-steps.md`. PR #10432 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/events.md`. PR #10693 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/cloud.md`. PR #10746 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/behind-a-proxy.md`. PR #10675 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/help-fastapi.md`. PR #10455 by @nilslindemann.
  * 🌐 Update German translation for `docs/de/docs/python-types.md`. PR #10287 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/path-params.md`. PR #10290 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/handling-errors.md`. PR #10379 by @nilslindemann.
  * 🌐 Update German translation for `docs/de/docs/index.md`. PR #10283 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/security/http-basic-auth.md`. PR #10651 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/bigger-applications.md`. PR #10554 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/path-operation-advanced-configuration.md`. PR #10612 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/static-files.md`. PR #10584 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/security/oauth2-jwt.md`. PR #10522 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/response-model.md`. PR #10345 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/extra-models.md`. PR #10351 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/body-updates.md`. PR #10396 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/alternatives.md`. PR #10855 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/templates.md`. PR #10678 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/security/oauth2-scopes.md`. PR #10643 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/async-tests.md`. PR #10708 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/metadata.md`. PR #10581 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/testing.md`. PR #10586 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/schema-extra-example.md`. PR #10597 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/index.md`. PR #10611 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/response-directly.md`. PR #10618 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/additional-responses.md`. PR #10626 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/response-cookies.md`. PR #10627 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/response-headers.md`. PR #10628 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/response-change-status-code.md`. PR #10632 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/advanced-dependencies.md`. PR #10633 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/security/index.md`. PR #10635 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/using-request-directly.md`. PR #10653 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/dataclasses.md`. PR #10667 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/middleware.md`. PR #10668 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/sub-applications.md`. PR #10671 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/websockets.md`. PR #10687 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/testing-websockets.md`. PR #10703 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/testing-events.md`. PR #10704 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/testing-dependencies.md`. PR #10706 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/openapi-callbacks.md`. PR #10710 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/settings.md`. PR #10709 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/wsgi.md`. PR #10713 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/index.md`. PR #10733 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/https.md`. PR #10737 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/manually.md`. PR #10738 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/concepts.md`. PR #10744 by @nilslindemann.
  * 🌐 Update German translation for `docs/de/docs/features.md`. PR #10284 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/server-workers.md`. PR #10747 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/docker.md`. PR #10759 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/index.md`. PR #10769 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/general.md`. PR #10770 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/graphql.md`. PR #10788 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/custom-request-and-route.md`. PR #10789 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/conditional-openapi.md`. PR #10790 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/separate-openapi-schemas.md`. PR #10796 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/configure-swagger-ui.md`. PR #10804 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/how-to/custom-docs-ui-assets.md`. PR #10803 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/parameters.md`. PR #10814 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/status.md`. PR #10815 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/uploadfile.md`. PR #10816 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/exceptions.md`. PR #10817 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/dependencies.md`. PR #10818 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/apirouter.md`. PR #10819 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/websockets.md`. PR #10822 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/httpconnection.md`. PR #10823 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/response.md`. PR #10824 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/middleware.md`. PR #10837 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/openapi/*.md`. PR #10838 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/security/index.md`. PR #10839 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/staticfiles.md`. PR #10841 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/testclient.md`. PR #10843 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/project-generation.md`. PR #10851 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/history-design-future.md`. PR #10865 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #10422 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/global-dependencies.md`. PR #10420 by @nilslindemann.
  * 🌐 Update German translation for `docs/de/docs/fastapi-people.md`. PR #10285 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/sub-dependencies.md`. PR #10409 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/security/index.md`. PR #10429 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #10411 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/extra-data-types.md`. PR #10534 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/security/simple-oauth2.md`. PR #10504 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/security/get-current-user.md`. PR #10439 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/request-forms-and-files.md`. PR #10368 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/encoder.md`. PR #10385 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/request-forms.md`. PR #10361 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/deployment/versions.md`. PR #10491 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/async.md`. PR #10449 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/cookie-params.md`. PR #10323 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #10407 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/dependencies/index.md`. PR #10399 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/header-params.md`. PR #10326 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/path-params-numeric-validations.md`. PR #10307 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/query-params-str-validations.md`. PR #10304 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/request-files.md`. PR #10364 by @nilslindemann.
  * :globe_with_meridians: Add Portuguese translation for `docs/pt/docs/advanced/templates.md`. PR #11338 by @SamuelBFavarin.
  * 🌐 Add Bengali translations for `docs/bn/docs/learn/index.md`. PR #11337 by @imtiaz101325.
  * 🌐 Fix Korean translation for `docs/ko/docs/index.md`. PR #11296 by @choi-haram.
  * 🌐 Add Korean translation for `docs/ko/docs/about/index.md`. PR #11299 by @choi-haram.
  * 🌐 Add Korean translation for `docs/ko/docs/advanced/index.md`. PR #9613 by @ElliottLarsen.
  * 🌐 Add German translation for `docs/de/docs/how-to/extending-openapi.md`. PR #10794 by @nilslindemann.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/metadata.md`. PR #11286 by @jackleeio.
  * 🌐 Update Chinese translation for `docs/zh/docs/contributing.md`. PR #10887 by @Aruelius.
  * 🌐 Add Azerbaijani translation for `docs/az/docs/fastapi-people.md`. PR #11195 by @vusallyv.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/index.md`. PR #11223 by @kohiry.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/query-params.md`. PR #11242 by @jackleeio.
  * 🌐 Add Azerbaijani translation for `docs/az/learn/index.md`. PR #11192 by @vusallyv.


### Internal¶
  * 👥 Update FastAPI People. PR #11387 by @tiangolo.
  * ⬆ Bump actions/cache from 3 to 4. PR #10988 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.8.11 to 1.8.14. PR #11318 by @dependabot[bot].
  * ⬆ Bump pillow from 10.1.0 to 10.2.0. PR #11011 by @dependabot[bot].
  * ⬆ Bump black from 23.3.0 to 24.3.0. PR #11325 by @dependabot[bot].
  * 👷 Add cron to run test once a week on monday. PR #11377 by @estebanx64.
  * ➕ Replace mkdocs-markdownextradata-plugin with mkdocs-macros-plugin. PR #11383 by @tiangolo.
  * 👷 Disable MkDocs insiders social plugin while an issue in MkDocs Material is handled. PR #11373 by @tiangolo.
  * 👷 Fix logic for when to install and use MkDocs Insiders. PR #11372 by @tiangolo.
  * 👷 Do not use Python packages cache for publish. PR #11366 by @tiangolo.
  * 👷 Add CI to test sdists for redistribution (e.g. Linux distros). PR #11365 by @tiangolo.
  * 👷 Update build-docs GitHub Action path filter. PR #11354 by @tiangolo.
  * 🔧 Update Ruff config, add extra ignore rule from SQLModel. PR #11353 by @tiangolo.
  * ⬆️ Upgrade configuration for Ruff v0.2.0. PR #11075 by @charliermarsh.
  * 🔧 Update sponsors, add MongoDB. PR #11346 by @tiangolo.
  * ⬆ Bump dorny/paths-filter from 2 to 3. PR #11028 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 3.0.0 to 3.1.4. PR #11310 by @dependabot[bot].
  * ♻️ Refactor computing FastAPI People, include 3 months, 6 months, 1 year, based on comment date, not discussion date. PR #11304 by @tiangolo.
  * 👥 Update FastAPI People. PR #11228 by @tiangolo.
  * 🔥 Remove Jina AI QA Bot from the docs. PR #11268 by @nan-wang.
  * 🔧 Update sponsors, remove Jina, remove Powens, move TestDriven.io. PR #11213 by @tiangolo.


## 0.110.0¶
### Breaking Changes¶
  * 🐛 Fix unhandled growing memory for internal server errors, refactor dependencies with `yield` and `except` to require raising again as in regular Python. PR #11191 by @tiangolo.
    * This is a breaking change (and only slightly) if you used dependencies with `yield`, used `except` in those dependencies, and didn't raise again.
    * This was reported internally by @rushilsrivastava as a memory leak when the server had unhandled exceptions that would produce internal server errors, the memory allocated before that point would not be released.
    * Read the new docs: Dependencies with `yield` and `except`.


In short, if you had dependencies that looked like:
```
defmy_dep():
  try:
    yield
  except SomeException:
    pass

```

Now you need to make sure you raise again after `except`, just as you would in regular Python:
```
defmy_dep():
  try:
    yield
  except SomeException:
    raise

```

### Docs¶
  * ✏️ Fix minor typos in `docs/ko/docs/`. PR #11126 by @KaniKim.
  * ✏️ Fix minor typo in `fastapi/applications.py`. PR #11099 by @JacobHayes.


### Translations¶
  * 🌐 Add German translation for `docs/de/docs/reference/background.md`. PR #10820 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/templating.md`. PR #10842 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/external-links.md`. PR #10852 by @nilslindemann.
  * 🌐 Update Turkish translation for `docs/tr/docs/tutorial/query-params.md`. PR #11162 by @hasansezertasan.
  * 🌐 Add German translation for `docs/de/docs/reference/encoders.md`. PR #10840 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/responses.md`. PR #10825 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/reference/request.md`. PR #10821 by @nilslindemann.
  * 🌐 Add Turkish translation for `docs/tr/docs/tutorial/query-params.md`. PR #11078 by @emrhnsyts.
  * 🌐 Add German translation for `docs/de/docs/reference/fastapi.md`. PR #10813 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/newsletter.md`. PR #10853 by @nilslindemann.
  * 🌐 Add Traditional Chinese translation for `docs/zh-hant/docs/learn/index.md`. PR #11142 by @hsuanchi.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/dependencies/global-dependencies.md`. PR #11123 by @riroan.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #11124 by @riroan.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/schema-extra-example.md`. PR #11121 by @KaniKim.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/body-fields.md`. PR #11112 by @KaniKim.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/cookie-params.md`. PR #11118 by @riroan.
  * 🌐 Update Korean translation for `/docs/ko/docs/dependencies/index.md`. PR #11114 by @KaniKim.
  * 🌐 Update Korean translation for `/docs/ko/docs/deployment/docker.md`. PR #11113 by @KaniKim.
  * 🌐 Update Turkish translation for `docs/tr/docs/tutorial/first-steps.md`. PR #11094 by @hasansezertasan.
  * 🌐 Add Spanish translation for `docs/es/docs/advanced/security/index.md`. PR #2278 by @Xaraxx.
  * 🌐 Add Spanish translation for `docs/es/docs/advanced/response-headers.md`. PR #2276 by @Xaraxx.
  * 🌐 Add Spanish translation for `docs/es/docs/deployment/index.md` and `~/deployment/versions.md`. PR #9669 by @pabloperezmoya.
  * 🌐 Add Spanish translation for `docs/es/docs/benchmarks.md`. PR #10928 by @pablocm83.
  * 🌐 Add Spanish translation for `docs/es/docs/advanced/response-change-status-code.md`. PR #11100 by @alejsdev.


## 0.109.2¶
### Upgrades¶
  * ⬆️ Upgrade version of Starlette to `>= 0.36.3`. PR #11086 by @tiangolo.


### Translations¶
  * 🌐 Update Turkish translation for `docs/tr/docs/fastapi-people.md`. PR #10547 by @alperiox.


### Internal¶
  * 🍱 Add new FastAPI logo. PR #11090 by @tiangolo.


## 0.109.1¶
### Security fixes¶
  * ⬆️ Upgrade minimum version of `python-multipart` to `>=0.0.7` to fix a vulnerability when using form data with a ReDos attack. You can also simply upgrade `python-multipart`.


Read more in the advisory: Content-Type Header ReDoS.
### Features¶
  * ✨ Include HTTP 205 in status codes with no body. PR #10969 by @tiangolo.


### Refactors¶
  * ✅ Refactor tests for duplicate operation ID generation for compatibility with other tools running the FastAPI test suite. PR #10876 by @emmettbutler.
  * ♻️ Simplify string format with f-strings in `fastapi/utils.py`. PR #10576 by @eukub.
  * 🔧 Fix Ruff configuration unintentionally enabling and re-disabling mccabe complexity check. PR #10893 by @jiridanek.
  * ✅ Re-enable test in `tests/test_tutorial/test_header_params/test_tutorial003.py` after fix in Starlette. PR #10904 by @ooknimm.


### Docs¶
  * 📝 Tweak wording in `help-fastapi.md`. PR #11040 by @tiangolo.
  * 📝 Tweak docs for Behind a Proxy. PR #11038 by @tiangolo.
  * 📝 Add External Link: 10 Tips for adding SQLAlchemy to FastAPI. PR #11036 by @Donnype.
  * 📝 Add External Link: Tips on migrating from Flask to FastAPI and vice-versa. PR #11029 by @jtemporal.
  * 📝 Deprecate old tutorials: Peewee, Couchbase, encode/databases. PR #10979 by @tiangolo.
  * ✏️ Fix typo in `fastapi/security/oauth2.py`. PR #10972 by @RafalSkolasinski.
  * 📝 Update `HTTPException` details in `docs/en/docs/tutorial/handling-errors.md`. PR #5418 by @papb.
  * ✏️ A few tweaks in `docs/de/docs/tutorial/first-steps.md`. PR #10959 by @nilslindemann.
  * ✏️ Fix link in `docs/en/docs/advanced/async-tests.md`. PR #10960 by @nilslindemann.
  * ✏️ Fix typos for Spanish documentation. PR #10957 by @jlopezlira.
  * 📝 Add warning about lifespan functions and backwards compatibility with events. PR #10734 by @jacob-indigo.
  * ✏️ Fix broken link in `docs/tutorial/sql-databases.md` in several languages. PR #10716 by @theoohoho.
  * ✏️ Remove broken links from `external_links.yml`. PR #10943 by @Torabek.
  * 📝 Update template docs with more info about `url_for`. PR #5937 by @EzzEddin.
  * 📝 Update usage of Token model in security docs. PR #9313 by @piotrszacilowski.
  * ✏️ Update highlighted line in `docs/en/docs/tutorial/bigger-applications.md`. PR #5490 by @papb.
  * 📝 Add External Link: Explore How to Effectively Use JWT With FastAPI. PR #10212 by @aanchlia.
  * 📝 Add hyperlink to `docs/en/docs/tutorial/static-files.md`. PR #10243 by @hungtsetse.
  * 📝 Add External Link: Instrument a FastAPI service adding tracing with OpenTelemetry and send/show traces in Grafana Tempo. PR #9440 by @softwarebloat.
  * 📝 Review and rewording of `en/docs/contributing.md`. PR #10480 by @nilslindemann.
  * 📝 Add External Link: ML serving and monitoring with FastAPI and Evidently. PR #9701 by @mnrozhkov.
  * 📝 Reword in docs, from "have in mind" to "keep in mind". PR #10376 by @malicious.
  * 📝 Add External Link: Talk by Jeny Sadadia. PR #10265 by @JenySadadia.
  * 📝 Add location info to `tutorial/bigger-applications.md`. PR #10552 by @nilslindemann.
  * ✏️ Fix Pydantic method name in `docs/en/docs/advanced/path-operation-advanced-configuration.md`. PR #10826 by @ahmedabdou14.


### Translations¶
  * 🌐 Add Spanish translation for `docs/es/docs/external-links.md`. PR #10933 by @pablocm83.
  * 🌐 Update Korean translation for `docs/ko/docs/tutorial/first-steps.md`, `docs/ko/docs/tutorial/index.md`, `docs/ko/docs/tutorial/path-params.md`, and `docs/ko/docs/tutorial/query-params.md`. PR #4218 by @SnowSuno.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #10870 by @zhiquanchi.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/concepts.md`. PR #10282 by @xzmeng.
  * 🌐 Add Azerbaijani translation for `docs/az/docs/index.md`. PR #11047 by @aykhans.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/middleware.md`. PR #2829 by @JeongHyeongKim.
  * 🌐 Add German translation for `docs/de/docs/tutorial/body-nested-models.md`. PR #10313 by @nilslindemann.
  * 🌐 Add Persian translation for `docs/fa/docs/tutorial/middleware.md`. PR #9695 by @mojtabapaso.
  * 🌐 Update Farsi translation for `docs/fa/docs/index.md`. PR #10216 by @theonlykingpin.
  * 🌐 Add German translation for `docs/de/docs/tutorial/body-fields.md`. PR #10310 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/body.md`. PR #10295 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/body-multiple-params.md`. PR #10308 by @nilslindemann.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/security/get-current-user.md`. PR #2681 by @sh0nk.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/advanced-dependencies.md`. PR #3798 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/events.md`. PR #3815 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/behind-a-proxy.md`. PR #3820 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/testing-events.md`. PR #3818 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/testing-websockets.md`. PR #3817 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/testing-database.md`. PR #3821 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/deta.md`. PR #3837 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/history-design-future.md`. PR #3832 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/project-generation.md`. PR #3831 by @jaystone776.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/docker.md`. PR #10296 by @xzmeng.
  * 🌐 Update Spanish translation for `docs/es/docs/features.md`. PR #10884 by @pablocm83.
  * 🌐 Add Spanish translation for `docs/es/docs/newsletter.md`. PR #10922 by @pablocm83.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/background-tasks.md`. PR #5910 by @junah201.
  * :globe_with_meridians: Add Turkish translation for `docs/tr/docs/alternatives.md`. PR #10502 by @alperiox.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/dependencies/index.md`. PR #10989 by @KaniKim.
  * 🌐 Add Korean translation for `/docs/ko/docs/tutorial/body.md`. PR #11000 by @KaniKim.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/schema-extra-example.md`. PR #4065 by @luccasmmg.
  * 🌐 Add Turkish translation for `docs/tr/docs/history-design-future.md`. PR #11012 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/resources/index.md`. PR #11020 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/how-to/index.md`. PR #11021 by @hasansezertasan.
  * 🌐 Add German translation for `docs/de/docs/tutorial/query-params.md`. PR #10293 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/benchmarks.md`. PR #10866 by @nilslindemann.
  * 🌐 Add Turkish translation for `docs/tr/docs/learn/index.md`. PR #11014 by @hasansezertasan.
  * 🌐 Add Persian translation for `docs/fa/docs/tutorial/security/index.md`. PR #9945 by @mojtabapaso.
  * 🌐 Add Turkish translation for `docs/tr/docs/help/index.md`. PR #11013 by @hasansezertasan.
  * 🌐 Add Turkish translation for `docs/tr/docs/about/index.md`. PR #11006 by @hasansezertasan.
  * 🌐 Update Turkish translation for `docs/tr/docs/benchmarks.md`. PR #11005 by @hasansezertasan.
  * 🌐 Add Italian translation for `docs/it/docs/index.md`. PR #5233 by @matteospanio.
  * 🌐 Add Korean translation for `docs/ko/docs/help/index.md`. PR #10983 by @KaniKim.
  * 🌐 Add Korean translation for `docs/ko/docs/features.md`. PR #10976 by @KaniKim.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/security/get-current-user.md`. PR #5737 by @KdHyeon0661.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/security/first-steps.md`. PR #10541 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/handling-errors.md`. PR #10375 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/encoder.md`. PR #10374 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/body-updates.md`. PR #10373 by @AlertRED.
  * 🌐 Russian translation: updated `fastapi-people.md`.. PR #10255 by @NiKuma0.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/security/index.md`. PR #5798 by @3w36zj6.
  * 🌐 Add German translation for `docs/de/docs/advanced/generate-clients.md`. PR #10725 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/openapi-webhooks.md`. PR #10712 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/custom-response.md`. PR #10624 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/advanced/additional-status-codes.md`. PR #10617 by @nilslindemann.
  * 🌐 Add German translation for `docs/de/docs/tutorial/middleware.md`. PR #10391 by @JohannesJungbluth.
  * 🌐 Add German translation for introduction documents. PR #10497 by @nilslindemann.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/encoder.md`. PR #1955 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/extra-data-types.md`. PR #1932 by @SwftAlpc.
  * 🌐 Add Turkish translation for `docs/tr/docs/async.md`. PR #5191 by @BilalAlpaslan.
  * 🌐 Add Turkish translation for `docs/tr/docs/project-generation.md`. PR #5192 by @BilalAlpaslan.
  * 🌐 Add Korean translation for `docs/ko/docs/deployment/docker.md`. PR #5657 by @nearnear.
  * 🌐 Add Korean translation for `docs/ko/docs/deployment/server-workers.md`. PR #4935 by @jujumilk3.
  * 🌐 Add Korean translation for `docs/ko/docs/deployment/index.md`. PR #4561 by @jujumilk3.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/path-operation-configuration.md`. PR #3639 by @jungsu-kwon.
  * 🌐 Modify the description of `zh` - Traditional Chinese. PR #10889 by @cherinyy.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/static-files.md`. PR #2957 by @jeesang7.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/response-model.md`. PR #2766 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/body-multiple-params.md`. PR #2461 by @PandaHun.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/query-params-str-validations.md`. PR #2415 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/python-types.md`. PR #2267 by @jrim.
  * 🌐 Add Korean translation for `docs/ko/docs/tutorial/body-nested-models.md`. PR #2506 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/learn/index.md`. PR #10977 by @KaniKim.
  * 🌐 Initialize translations for Traditional Chinese. PR #10505 by @hsuanchi.
  * ✏️ Tweak the german translation of `docs/de/docs/tutorial/index.md`. PR #10962 by @nilslindemann.
  * ✏️ Fix typo error in `docs/ko/docs/tutorial/path-params.md`. PR #10758 by @2chanhaeng.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #1961 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #1960 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/dependencies/sub-dependencies.md`. PR #1959 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/background-tasks.md`. PR #2668 by @tokusumi.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/dependencies/index.md` and `docs/ja/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #1958 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/response-model.md`. PR #1938 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/body-multiple-params.md`. PR #1903 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/path-params-numeric-validations.md`. PR #1902 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/python-types.md`. PR #1899 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/handling-errors.md`. PR #1953 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/response-status-code.md`. PR #1942 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/extra-models.md`. PR #1941 by @SwftAlpc.
  * 🌐 Add Japanese tranlsation for `docs/ja/docs/tutorial/schema-extra-example.md`. PR #1931 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/body-nested-models.md`. PR #1930 by @SwftAlpc.
  * 🌐 Add Japanese translation for `docs/ja/docs/tutorial/body-fields.md`. PR #1923 by @SwftAlpc.
  * 🌐 Add German translation for `docs/de/docs/tutorial/index.md`. PR #9502 by @fhabers21.
  * 🌐 Add German translation for `docs/de/docs/tutorial/background-tasks.md`. PR #10566 by @nilslindemann.
  * ✏️ Fix typo in `docs/ru/docs/index.md`. PR #10672 by @Delitel-WEB.
  * ✏️ Fix typos in `docs/zh/docs/tutorial/extra-data-types.md`. PR #10727 by @HiemalBeryl.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #10410 by @AlertRED.


### Internal¶
  * 👥 Update FastAPI People. PR #11074 by @tiangolo.
  * 🔧 Update sponsors: add Coherence. PR #11066 by @tiangolo.
  * 👷 Upgrade GitHub Action issue-manager. PR #11056 by @tiangolo.
  * 🍱 Update sponsors: TalkPython badge. PR #11052 by @tiangolo.
  * 🔧 Update sponsors: TalkPython badge image. PR #11048 by @tiangolo.
  * 🔧 Update sponsors, remove Deta. PR #11041 by @tiangolo.
  * 💄 Fix CSS breaking RTL languages (erroneously introduced by a previous RTL PR). PR #11039 by @tiangolo.
  * 🔧 Add Italian to `mkdocs.yml`. PR #11016 by @alejsdev.
  * 🔨 Verify `mkdocs.yml` languages in CI, update `docs.py`. PR #11009 by @tiangolo.
  * 🔧 Update config in `label-approved.yml` to accept translations with 1 reviewer. PR #11007 by @alejsdev.
  * 👷 Add changes-requested handling in GitHub Action issue manager. PR #10971 by @tiangolo.
  * 🔧 Group dependencies on dependabot updates. PR #10952 by @Kludex.
  * ⬆ Bump actions/setup-python from 4 to 5. PR #10764 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.8.10 to 1.8.11. PR #10731 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.28.0 to 3.0.0. PR #10777 by @dependabot[bot].
  * 🔧 Add support for translations to languages with a longer code name, like `zh-hant`. PR #10950 by @tiangolo.


## 0.109.0¶
### Features¶
  * ✨ Add support for Python 3.12. PR #10666 by @Jamim.


### Upgrades¶
  * ⬆️ Upgrade Starlette to >=0.35.0,<0.36.0. PR #10938 by @tiangolo.


### Docs¶
  * ✏️ Fix typo in `docs/en/docs/alternatives.md`. PR #10931 by @s111d.
  * 📝 Replace `email` with `username` in `docs_src/security/tutorial007` code examples. PR #10649 by @nilslindemann.
  * 📝 Add VS Code tutorial link. PR #10592 by @nilslindemann.
  * 📝 Add notes about Pydantic v2's new `.model_dump()`. PR #10929 by @tiangolo.
  * 📝 Fix broken link in `docs/en/docs/tutorial/sql-databases.md`. PR #10765 by @HurSungYun.
  * 📝 Add External Link: FastAPI application monitoring made easy. PR #10917 by @tiangolo.
  * ✨ Generate automatic language names for docs translations. PR #5354 by @jakul.
  * ✏️ Fix typos in `docs/en/docs/alternatives.md` and `docs/en/docs/tutorial/dependencies/index.md`. PR #10906 by @s111d.
  * ✏️ Fix typos in `docs/en/docs/tutorial/dependencies/dependencies-with-yield.md`. PR #10834 by @Molkree.
  * 📝 Add article: "Building a RESTful API with FastAPI: Secure Signup and Login Functionality Included". PR #9733 by @dxphilo.
  * 📝 Add warning about lifecycle events with `AsyncClient`. PR #4167 by @andrew-chang-dewitt.
  * ✏️ Fix typos in `/docs/reference/exceptions.md` and `/en/docs/reference/status.md`. PR #10809 by @clarencepenz.
  * ✏️ Fix typo in `openapi-callbacks.md`. PR #10673 by @kayjan.
  * ✏️ Fix typo in `fastapi/routing.py` . PR #10520 by @sepsh.
  * 📝 Replace HTTP code returned in case of existing user error in docs for testing. PR #4482 by @TristanMarion.
  * 📝 Add blog for FastAPI & Supabase. PR #6018 by @theinfosecguy.
  * 📝 Update example source files for SQL databases with SQLAlchemy. PR #9508 by @s-mustafa.
  * 📝 Update code examples in docs for body, replace name `create_item` with `update_item` when appropriate. PR #5913 by @OttoAndrey.
  * ✏️ Fix typo in dependencies with yield source examples. PR #10847 by @tiangolo.


### Translations¶
  * 🌐 Add Bengali translation for `docs/bn/docs/index.md`. PR #9177 by @Fahad-Md-Kamal.
  * ✏️ Update Python version in `index.md` in several languages. PR #10711 by @tamago3keran.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/request-forms-and-files.md`. PR #10347 by @AlertRED.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/index.md`. PR #10362 by @rostik1410.
  * ✏️ Update Python version in `docs/ko/docs/index.md`. PR #10680 by @Eeap.
  * 🌐 Add Persian translation for `docs/fa/docs/features.md`. PR #5887 by @amirilf.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/additional-responses.md`. PR #10325 by @ShuibeiC.
  * 🌐 Fix typos in Russian translations for `docs/ru/docs/tutorial/background-tasks.md`, `docs/ru/docs/tutorial/body-nested-models.md`, `docs/ru/docs/tutorial/debugging.md`, `docs/ru/docs/tutorial/testing.md`. PR #10311 by @AlertRED.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/request-files.md`. PR #10332 by @AlertRED.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/server-workers.md`. PR #10292 by @xzmeng.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/cloud.md`. PR #10291 by @xzmeng.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/manually.md`. PR #10279 by @xzmeng.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/https.md`. PR #10277 by @xzmeng.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/index.md`. PR #10275 by @xzmeng.
  * 🌐 Add German translation for `docs/de/docs/tutorial/first-steps.md`. PR #9530 by @fhabers21.
  * 🌐 Update Turkish translation for `docs/tr/docs/index.md`. PR #10444 by @hasansezertasan.
  * 🌐 Add Chinese translation for `docs/zh/docs/learn/index.md`. PR #10479 by @KAZAMA-DREAM.
  * 🌐 Add Russian translation for `docs/ru/docs/learn/index.md`. PR #10539 by @AlertRED.
  * 🌐 Update SQLAlchemy instruction in Chinese translation `docs/zh/docs/tutorial/sql-databases.md`. PR #9712 by @Royc30ne.
  * 🌐 Add Turkish translation for `docs/tr/docs/external-links.md`. PR #10549 by @hasansezertasan.
  * 🌐 Add Spanish translation for `docs/es/docs/learn/index.md`. PR #10885 by @pablocm83.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/body-fields.md`. PR #10670 by @ArtemKhymenko.
  * 🌐 Add Hungarian translation for `/docs/hu/docs/index.md`. PR #10812 by @takacs.
  * 🌐 Add Turkish translation for `docs/tr/docs/newsletter.md`. PR #10550 by @hasansezertasan.
  * 🌐 Add Spanish translation for `docs/es/docs/help/index.md`. PR #10907 by @pablocm83.
  * 🌐 Add Spanish translation for `docs/es/docs/about/index.md`. PR #10908 by @pablocm83.
  * 🌐 Add Spanish translation for `docs/es/docs/resources/index.md`. PR #10909 by @pablocm83.


### Internal¶
  * 👥 Update FastAPI People. PR #10871 by @tiangolo.
  * 👷 Upgrade custom GitHub Action comment-docs-preview-in-pr. PR #10916 by @tiangolo.
  * ⬆️ Upgrade GitHub Action latest-changes. PR #10915 by @tiangolo.
  * 👷 Upgrade GitHub Action label-approved. PR #10913 by @tiangolo.
  * ⬆️ Upgrade GitHub Action label-approved. PR #10905 by @tiangolo.


## 0.108.0¶
### Upgrades¶
  * ⬆️ Upgrade Starlette to `>=0.29.0,<0.33.0`, update docs and usage of templates with new Starlette arguments. Remove pin of AnyIO `>=3.7.1,<4.0.0`, add support for AnyIO 4.x.x. PR #10846 by @tiangolo.


## 0.107.0¶
### Upgrades¶
  * ⬆️ Upgrade Starlette to 0.28.0. PR #9636 by @adriangb.


### Docs¶
  * 📝 Add docs: Node.js script alternative to update OpenAPI for generated clients. PR #10845 by @alejsdev.
  * 📝 Restructure Docs section in Contributing page. PR #10844 by @alejsdev.


## 0.106.0¶
### Breaking Changes¶
Using resources from dependencies with `yield` in background tasks is no longer supported.
This change is what supports the new features, read below. 🤓
### Dependencies with `yield`, `HTTPException` and Background Tasks¶
Dependencies with `yield` now can raise `HTTPException` and other exceptions after `yield`. 🎉
Read the new docs here: Dependencies with `yield` and `HTTPException`.
```
fromfastapiimport Depends, FastAPI, HTTPException
fromtyping_extensionsimport Annotated
app = FastAPI()
data = {
  "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
  "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}
classOwnerError(Exception):
  pass
defget_username():
  try:
    yield "Rick"
  except OwnerError as e:
    raise HTTPException(status_code=400, detail=f"Owner error: {e}")
@app.get("/items/{item_id}")
defget_item(item_id: str, username: Annotated[str, Depends(get_username)]):
  if item_id not in data:
    raise HTTPException(status_code=404, detail="Item not found")
  item = data[item_id]
  if item["owner"] != username:
    raise OwnerError(username)
  return item

```

Before FastAPI 0.106.0, raising exceptions after `yield` was not possible, the exit code in dependencies with `yield` was executed _after_ the response was sent, so Exception Handlers would have already run.
This was designed this way mainly to allow using the same objects "yielded" by dependencies inside of background tasks, because the exit code would be executed after the background tasks were finished.
Nevertheless, as this would mean waiting for the response to travel through the network while unnecessarily holding a resource in a dependency with yield (for example a database connection), this was changed in FastAPI 0.106.0.
Additionally, a background task is normally an independent set of logic that should be handled separately, with its own resources (e.g. its own database connection).
If you used to rely on this behavior, now you should create the resources for background tasks inside the background task itself, and use internally only data that doesn't depend on the resources of dependencies with `yield`.
For example, instead of using the same database session, you would create a new database session inside of the background task, and you would obtain the objects from the database using this new session. And then instead of passing the object from the database as a parameter to the background task function, you would pass the ID of that object and then obtain the object again inside the background task function.
The sequence of execution before FastAPI 0.106.0 was like this diagram:
Time flows from top to bottom. And each column is one of the parts interacting or executing code.
```
sequenceDiagram
participant client as Client
participant handler as Exception handler
participant dep as Dep with yield
participant operation as Path Operation
participant tasks as Background tasks
  Note over client,tasks: Can raise exception for dependency, handled after response is sent
  Note over client,operation: Can raise HTTPException and can change the response
  client ->> dep: Start request
  Note over dep: Run code up to yield
  opt raise
    dep -->> handler: Raise HTTPException
    handler -->> client: HTTP error response
    dep -->> dep: Raise other exception
  end
  dep ->> operation: Run dependency, e.g. DB session
  opt raise
    operation -->> dep: Raise HTTPException
    dep -->> handler: Auto forward exception
    handler -->> client: HTTP error response
    operation -->> dep: Raise other exception
    dep -->> handler: Auto forward exception
  end
  operation ->> client: Return response to client
  Note over client,operation: Response is already sent, can't change it anymore
  opt Tasks
    operation -->> tasks: Send background tasks
  end
  opt Raise other exception
    tasks -->> dep: Raise other exception
  end
  Note over dep: After yield
  opt Handle other exception
    dep -->> dep: Handle exception, can't change response. E.g. close DB session.
  end
```

The new execution flow can be found in the docs: Execution of dependencies with `yield`.
### Features¶
  * ✨ Add support for raising exceptions (including `HTTPException`) in dependencies with `yield` in the exit code, do not support them in background tasks. PR #10831 by @tiangolo.


### Internal¶
  * 👥 Update FastAPI People. PR #10567 by @tiangolo.


## 0.105.0¶
### Features¶
  * ✨ Add support for multiple Annotated annotations, e.g. `Annotated[str, Field(), Query()]`. PR #10773 by @tiangolo.


### Refactors¶
  * 🔥 Remove unused NoneType. PR #10774 by @tiangolo.


### Docs¶
  * 📝 Tweak default suggested configs for generating clients. PR #10736 by @tiangolo.


### Internal¶
  * 🔧 Update sponsors, add Scalar. PR #10728 by @tiangolo.
  * 🔧 Update sponsors, add PropelAuth. PR #10760 by @tiangolo.
  * 👷 Update build docs, verify README on CI. PR #10750 by @tiangolo.
  * 🔧 Update sponsors, remove Fern. PR #10729 by @tiangolo.
  * 🔧 Update sponsors, add Codacy. PR #10677 by @tiangolo.
  * 🔧 Update sponsors, add Reflex. PR #10676 by @tiangolo.
  * 📝 Update release notes, move and check latest-changes. PR #10588 by @tiangolo.
  * 👷 Upgrade latest-changes GitHub Action. PR #10587 by @tiangolo.


## 0.104.1¶
### Fixes¶
  * 📌 Pin Swagger UI version to 5.9.0 temporarily to handle a bug crashing it in 5.9.1. PR #10529 by @alejandraklachquin.
    * This is not really a bug in FastAPI but in Swagger UI, nevertheless pinning the version will work while a solution is found on the Swagger UI side.


### Docs¶
  * 📝 Update data structure and render for external-links. PR #10495 by @tiangolo.
  * ✏️ Fix link to SPDX license identifier in `docs/en/docs/tutorial/metadata.md`. PR #10433 by @worldworm.
  * 📝 Update example validation error from Pydantic v1 to match Pydantic v2 in `docs/en/docs/tutorial/path-params.md`. PR #10043 by @giuliowaitforitdavide.
  * ✏️ Fix typos in emoji docs and in some source examples. PR #10438 by @afuetterer.
  * ✏️ Fix typo in `docs/en/docs/reference/dependencies.md`. PR #10465 by @suravshresth.
  * ✏️ Fix typos and rewordings in `docs/en/docs/tutorial/body-nested-models.md`. PR #10468 by @yogabonito.
  * 📝 Update docs, remove references to removed `pydantic.Required` in `docs/en/docs/tutorial/query-params-str-validations.md`. PR #10469 by @yogabonito.
  * ✏️ Fix typo in `docs/en/docs/reference/index.md`. PR #10467 by @tarsil.
  * 🔥 Remove unnecessary duplicated docstrings. PR #10484 by @tiangolo.


### Internal¶
  * ✏️ Update Pydantic links to dotenv support. PR #10511 by @White-Mask.
  * ✏️ Update links in `docs/en/docs/async.md` and `docs/zh/docs/async.md` to make them relative. PR #10498 by @hasnatsajid.
  * ✏️ Fix links in `docs/em/docs/async.md`. PR #10507 by @hasnatsajid.
  * ✏️ Fix typo in `docs/em/docs/index.md`, Python 3.8. PR #10521 by @kerriop.
  * ⬆ Bump pillow from 9.5.0 to 10.1.0. PR #10446 by @dependabot[bot].
  * ⬆ Update mkdocs-material requirement from <9.0.0,>=8.1.4 to >=8.1.4,<10.0.0. PR #5862 by @dependabot[bot].
  * ⬆ Bump mkdocs-material from 9.1.21 to 9.4.7. PR #10545 by @dependabot[bot].
  * 👷 Install MkDocs Material Insiders only when secrets are available, for Dependabot. PR #10544 by @tiangolo.
  * 🔧 Update sponsors badges, Databento. PR #10519 by @tiangolo.
  * 👷 Adopt Ruff format. PR #10517 by @tiangolo.
  * 🔧 Add `CITATION.cff` file for academic citations. PR #10496 by @tiangolo.
  * 🐛 Fix overriding MKDocs theme lang in hook. PR #10490 by @tiangolo.
  * 🔥 Drop/close Gitter chat. Questions should go to GitHub Discussions, free conversations to Discord.. PR #10485 by @tiangolo.


## 0.104.0¶
## Features¶
  * ✨ Add reference (code API) docs with PEP 727, add subclass with custom docstrings for `BackgroundTasks`, refactor docs structure. PR #10392 by @tiangolo. New docs at FastAPI Reference - Code API.


## Upgrades¶
  * ⬆️ Drop support for Python 3.7, require Python 3.8 or above. PR #10442 by @tiangolo.


### Internal¶
  * ⬆ Bump dawidd6/action-download-artifact from 2.27.0 to 2.28.0. PR #10268 by @dependabot[bot].
  * ⬆ Bump actions/checkout from 3 to 4. PR #10208 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.8.6 to 1.8.10. PR #10061 by @dependabot[bot].
  * 🔧 Update sponsors, Bump.sh images. PR #10381 by @tiangolo.
  * 👥 Update FastAPI People. PR #10363 by @tiangolo.


## 0.103.2¶
### Refactors¶
  * ⬆️ Upgrade compatibility with Pydantic v2.4, new renamed functions and JSON Schema input/output models with default values. PR #10344 by @tiangolo.


### Translations¶
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/extra-data-types.md`. PR #10132 by @ArtemKhymenko.
  * 🌐 Fix typos in French translations for `docs/fr/docs/advanced/path-operation-advanced-configuration.md`, `docs/fr/docs/alternatives.md`, `docs/fr/docs/async.md`, `docs/fr/docs/features.md`, `docs/fr/docs/help-fastapi.md`, `docs/fr/docs/index.md`, `docs/fr/docs/python-types.md`, `docs/fr/docs/tutorial/body.md`, `docs/fr/docs/tutorial/first-steps.md`, `docs/fr/docs/tutorial/query-params.md`. PR #10154 by @s-rigaud.
  * 🌐 Add Chinese translation for `docs/zh/docs/async.md`. PR #5591 by @mkdir700.
  * 🌐 Update Chinese translation for `docs/tutorial/security/simple-oauth2.md`. PR #3844 by @jaystone776.
  * 🌐 Add Korean translation for `docs/ko/docs/deployment/cloud.md`. PR #10191 by @Sion99.
  * 🌐 Add Japanese translation for `docs/ja/docs/deployment/https.md`. PR #10298 by @tamtam-fitness.
  * 🌐 Fix typo in Russian translation for `docs/ru/docs/tutorial/body-fields.md`. PR #10224 by @AlertRED.
  * 🌐 Add Polish translation for `docs/pl/docs/help-fastapi.md`. PR #10121 by @romabozhanovgithub.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/header-params.md`. PR #10226 by @AlertRED.
  * 🌐 Add Chinese translation for `docs/zh/docs/deployment/versions.md`. PR #10276 by @xzmeng.


### Internal¶
  * 🔧 Update sponsors, remove Flint. PR #10349 by @tiangolo.
  * 🔧 Rename label "awaiting review" to "awaiting-review" to simplify search queries. PR #10343 by @tiangolo.
  * 🔧 Update sponsors, enable Svix (revert #10228). PR #10253 by @tiangolo.
  * 🔧 Update sponsors, remove Svix. PR #10228 by @tiangolo.
  * 🔧 Update sponsors, add Bump.sh. PR #10227 by @tiangolo.


## 0.103.1¶
### Fixes¶
  * 📌 Pin AnyIO to < 4.0.0 to handle an incompatibility while upgrading to Starlette 0.31.1. PR #10194 by @tiangolo.


### Docs¶
  * ✏️ Fix validation parameter name in docs, from `regex` to `pattern`. PR #10085 by @pablodorrio.
  * ✏️ Fix indent format in `docs/en/docs/deployment/server-workers.md`. PR #10066 by @tamtam-fitness.
  * ✏️ Fix Pydantic examples in tutorial for Python types. PR #9961 by @rahulsalgare.
  * ✏️ Fix link to Pydantic docs in `docs/en/docs/tutorial/extra-data-types.md`. PR #10155 by @hasnatsajid.
  * ✏️ Fix typo in `docs/en/docs/tutorial/handling-errors.md`. PR #10170 by @poupapaa.
  * ✏️ Fix typo in `docs/en/docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #10172 by @ragul-kachiappan.


### Translations¶
  * 🌐 Remove duplicate line in translation for `docs/pt/docs/tutorial/path-params.md`. PR #10126 by @LecoOliveira.
  * 🌐 Add Yoruba translation for `docs/yo/docs/index.md`. PR #10033 by @AfolabiOlaoluwa.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/python-types.md`. PR #10080 by @rostik1410.
  * 🌐 Add Vietnamese translations for `docs/vi/docs/tutorial/first-steps.md` and `docs/vi/docs/tutorial/index.md`. PR #10088 by @magiskboy.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/alternatives.md`. PR #10060 by @whysage.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/index.md`. PR #10079 by @rostik1410.
  * ✏️ Fix typos in `docs/en/docs/how-to/separate-openapi-schemas.md` and `docs/en/docs/tutorial/schema-extra-example.md`. PR #10189 by @xzmeng.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/generate-clients.md`. PR #9883 by @funny-cat-happy.


### Refactors¶
  * ✏️ Fix typos in comment in `fastapi/applications.py`. PR #10045 by @AhsanSheraz.
  * ✅ Add missing test for OpenAPI examples, it was missing in coverage. PR #10188 by @tiangolo.


### Internal¶
  * 👥 Update FastAPI People. PR #10186 by @tiangolo.


## 0.103.0¶
### Features¶
  * ✨ Add support for `openapi_examples` in all FastAPI parameters. PR #10152 by @tiangolo.
    * New docs: OpenAPI-specific examples.


### Docs¶
  * 📝 Add note to docs about Separate Input and Output Schemas with FastAPI version. PR #10150 by @tiangolo.


## 0.102.0¶
### Features¶
  * ✨ Add support for disabling the separation of input and output JSON Schemas in OpenAPI with Pydantic v2 with `separate_input_output_schemas=False`. PR #10145 by @tiangolo.
    * New docs Separate OpenAPI Schemas for Input and Output or Not.
    * This PR also includes a new setup (internal tools) for generating screenshots for the docs.


### Refactors¶
  * ♻️ Refactor tests for new Pydantic 2.2.1. PR #10115 by @tiangolo.


### Docs¶
  * 📝 Add new docs section, How To - Recipes, move docs that don't have to be read by everyone to How To. PR #10114 by @tiangolo.
  * 📝 Update Advanced docs, add links to sponsor courses. PR #10113 by @tiangolo.
  * 📝 Update docs for generating clients. PR #10112 by @tiangolo.
  * 📝 Tweak MkDocs and add redirects. PR #10111 by @tiangolo.
  * 📝 Restructure docs for cloud providers, include links to sponsors. PR #10110 by @tiangolo.


### Internal¶
  * 🔧 Update sponsors, add Speakeasy. PR #10098 by @tiangolo.


## 0.101.1¶
### Fixes¶
  * ✨ Add `ResponseValidationError` printable details, to show up in server error logs. PR #10078 by @tiangolo.


### Refactors¶
  * ✏️ Fix typo in deprecation warnings in `fastapi/params.py`. PR #9854 by @russbiggs.
  * ✏️ Fix typos in comments on internal code in `fastapi/concurrency.py` and `fastapi/routing.py`. PR #9590 by @ElliottLarsen.


### Docs¶
  * ✏️ Fix typo in release notes. PR #9835 by @francisbergin.
  * 📝 Add external article: Build an SMS Spam Classifier Serverless Database with FaunaDB and FastAPI. PR #9847 by @adejumoridwan.
  * 📝 Fix typo in `docs/en/docs/contributing.md`. PR #9878 by @VicenteMerino.
  * 📝 Fix code highlighting in `docs/en/docs/tutorial/bigger-applications.md`. PR #9806 by @theonlykingpin.


### Translations¶
  * 🌐 Add Japanese translation for `docs/ja/docs/deployment/concepts.md`. PR #10062 by @tamtam-fitness.
  * 🌐 Add Japanese translation for `docs/ja/docs/deployment/server-workers.md`. PR #10064 by @tamtam-fitness.
  * 🌐 Update Japanese translation for `docs/ja/docs/deployment/docker.md`. PR #10073 by @tamtam-fitness.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/fastapi-people.md`. PR #10059 by @rostik1410.
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/cookie-params.md`. PR #10032 by @rostik1410.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/docker.md`. PR #9971 by @Xewus.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/python-types.md`. PR #10047 by @magiskboy.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/dependencies/global-dependencies.md`. PR #9970 by @dudyaosuplayer.
  * 🌐 Add Urdu translation for `docs/ur/docs/benchmarks.md`. PR #9974 by @AhsanSheraz.


### Internal¶
  * 🔧 Add sponsor Porter. PR #10051 by @tiangolo.
  * 🔧 Update sponsors, add Jina back as bronze sponsor. PR #10050 by @tiangolo.
  * ⬆ Bump mypy from 1.4.0 to 1.4.1. PR #9756 by @dependabot[bot].
  * ⬆ Bump mkdocs-material from 9.1.17 to 9.1.21. PR #9960 by @dependabot[bot].


## 0.101.0¶
### Features¶
  * ✨ Enable Pydantic's serialization mode for responses, add support for Pydantic's `computed_field`, better OpenAPI for response models, proper required attributes, better generated clients. PR #10011 by @tiangolo.


### Refactors¶
  * ✅ Fix tests for compatibility with pydantic 2.1.1. PR #9943 by @dmontagu.
  * ✅ Fix test error in Windows for `jsonable_encoder`. PR #9840 by @iudeen.


### Upgrades¶
  * 📌 Do not allow Pydantic 2.1.0 that breaks (require 2.1.1). PR #10012 by @tiangolo.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/security/index.md`. PR #9963 by @eVery1337.
  * 🌐 Remove Vietnamese note about missing translation. PR #9957 by @tiangolo.


### Internal¶
  * 👷 Add GitHub Actions step dump context to debug external failures. PR #10008 by @tiangolo.
  * 🔧 Restore MkDocs Material pin after the fix. PR #10001 by @tiangolo.
  * 🔧 Update the Question template to ask for the Pydantic version. PR #10000 by @tiangolo.
  * 📍 Update MkDocs Material dependencies. PR #9986 by @tiangolo.
  * 👥 Update FastAPI People. PR #9999 by @tiangolo.
  * 🐳 Update Dockerfile with compatibility versions, to upgrade later. PR #9998 by @tiangolo.
  * ➕ Add pydantic-settings to FastAPI People dependencies. PR #9988 by @tiangolo.
  * ♻️ Update FastAPI People logic with new Pydantic. PR #9985 by @tiangolo.
  * 🍱 Update sponsors, Fern badge. PR #9982 by @tiangolo.
  * 👷 Deploy docs to Cloudflare Pages. PR #9978 by @tiangolo.
  * 🔧 Update sponsor Fern. PR #9979 by @tiangolo.
  * 👷 Update CI debug mode with Tmate. PR #9977 by @tiangolo.


## 0.100.1¶
### Fixes¶
  * 🐛 Replace `MultHostUrl` to `AnyUrl` for compatibility with older versions of Pydantic v1. PR #9852 by @Kludex.


### Docs¶
  * 📝 Update links for self-hosted Swagger UI, point to v5, for OpenAPI 31.0. PR #9834 by @tiangolo.


### Translations¶
  * 🌐 Add Ukrainian translation for `docs/uk/docs/tutorial/body.md`. PR #4574 by @ss-o-furda.
  * 🌐 Add Vietnamese translation for `docs/vi/docs/features.md` and `docs/vi/docs/index.md`. PR #3006 by @magiskboy.
  * 🌐 Add Korean translation for `docs/ko/docs/async.md`. PR #4179 by @NinaHwang.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/background-tasks.md`. PR #9812 by @wdh99.
  * 🌐 Add French translation for `docs/fr/docs/tutorial/query-params-str-validations.md`. PR #4075 by @Smlep.
  * 🌐 Add French translation for `docs/fr/docs/tutorial/index.md`. PR #2234 by @JulianMaurin.
  * 🌐 Add French translation for `docs/fr/docs/contributing.md`. PR #2132 by @JulianMaurin.
  * 🌐 Add French translation for `docs/fr/docs/benchmarks.md`. PR #2155 by @clemsau.
  * 🌐 Update Chinese translations with new source files. PR #9738 by @mahone3297.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/request-forms.md`. PR #9841 by @dedkot01.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/handling-errors.md`. PR #9485 by @Creat55.


### Internal¶
  * 🔧 Update sponsors, add Fern. PR #9956 by @tiangolo.
  * 👷 Update FastAPI People token. PR #9844 by @tiangolo.
  * 👥 Update FastAPI People. PR #9775 by @tiangolo.
  * 👷 Update MkDocs Material token. PR #9843 by @tiangolo.
  * 👷 Update token for latest changes. PR #9842 by @tiangolo.


## 0.100.0¶
✨ Support for **Pydantic v2** ✨
Pydantic version 2 has the **core** re-written in **Rust** and includes a lot of improvements and features, for example:
  * Improved **correctness** in corner cases.
  * **Safer** types.
  * Better **performance** and **less energy** consumption.
  * Better **extensibility**.
  * etc.


...all this while keeping the **same Python API**. In most of the cases, for simple models, you can simply upgrade the Pydantic version and get all the benefits. 🚀
In some cases, for pure data validation and processing, you can get performance improvements of **20x** or more. This means 2,000% or more. 🤯
When you use **FastAPI** , there's a lot more going on, processing the request and response, handling dependencies, executing **your own code** , and particularly, **waiting for the network**. But you will probably still get some nice performance improvements just from the upgrade.
The focus of this release is **compatibility** with Pydantic v1 and v2, to make sure your current apps keep working. Later there will be more focus on refactors, correctness, code improvements, and then **performance** improvements. Some third-party early beta testers that ran benchmarks on the beta releases of FastAPI reported improvements of **2x - 3x**. Which is not bad for just doing `pip install --upgrade fastapi pydantic`. This was not an official benchmark and I didn't check it myself, but it's a good sign.
### Migration¶
Check out the Pydantic migration guide.
For the things that need changes in your Pydantic models, the Pydantic team built `bump-pydantic`.
A command line tool that will **process your code** and update most of the things **automatically** for you. Make sure you have your code in git first, and review each of the changes to make sure everything is correct before committing the changes.
### Pydantic v1¶
**This version of FastAPI still supports Pydantic v1**. And although Pydantic v1 will be deprecated at some point, it will still be supported for a while.
This means that you can install the new Pydantic v2, and if something fails, you can install Pydantic v1 while you fix any problems you might have, but having the latest FastAPI.
There are **tests for both Pydantic v1 and v2** , and test **coverage** is kept at **100%**.
### Changes¶
  * There are **new parameter** fields supported by Pydantic `Field()` for:
    * `Path()`
    * `Query()`
    * `Header()`
    * `Cookie()`
    * `Body()`
    * `Form()`
    * `File()`
  * The new parameter fields are:
    * `default_factory`
    * `alias_priority`
    * `validation_alias`
    * `serialization_alias`
    * `discriminator`
    * `strict`
    * `multiple_of`
    * `allow_inf_nan`
    * `max_digits`
    * `decimal_places`
    * `json_schema_extra`


...you can read about them in the Pydantic docs.
  * The parameter `regex` has been deprecated and replaced by `pattern`.
    * You can read more about it in the docs for Query Parameters and String Validations: Add regular expressions.
  * New Pydantic models use an improved and simplified attribute `model_config` that takes a simple dict instead of an internal class `Config` for their configuration.
    * You can read more about it in the docs for Declare Request Example Data.
  * The attribute `schema_extra` for the internal class `Config` has been replaced by the key `json_schema_extra` in the new `model_config` dict.
    * You can read more about it in the docs for Declare Request Example Data.
  * When you install `"fastapi[all]"` it now also includes:
    * `pydantic-settings` - for settings management.
    * `pydantic-extra-types` - for extra types to be used with Pydantic.
  * Now Pydantic Settings is an additional optional package (included in `"fastapi[all]"`). To use settings you should now import `from pydantic_settings import BaseSettings` instead of importing from `pydantic` directly.
    * You can read more about it in the docs for Settings and Environment Variables.
  * PR #9816 by @tiangolo, included all the work done (in multiple PRs) on the beta branch (`main-pv2`).


## 0.99.1¶
### Fixes¶
  * 🐛 Fix JSON Schema accepting bools as valid JSON Schemas, e.g. `additionalProperties: false`. PR #9781 by @tiangolo.


### Docs¶
  * 📝 Update source examples to use new JSON Schema examples field. PR #9776 by @tiangolo.


## 0.99.0¶
### Features¶
  * ✨ Add support for OpenAPI 3.1.0. PR #9770 by @tiangolo.
    * New support for documenting **webhooks** , read the new docs here: Advanced User Guide: OpenAPI Webhooks.
    * Upgrade OpenAPI 3.1.0, this uses JSON Schema 2020-12.
    * Upgrade Swagger UI to version 5.x.x, that supports OpenAPI 3.1.0.
    * Updated `examples` field in `Query()`, `Cookie()`, `Body()`, etc. based on the latest JSON Schema and OpenAPI. Now it takes a list of examples and they are included directly in the JSON Schema, not outside. Read more about it (including the historical technical details) in the updated docs: Tutorial: Declare Request Example Data.
  * ✨ Add support for `deque` objects and children in `jsonable_encoder`. PR #9433 by @cranium.


### Docs¶
  * 📝 Fix form for the FastAPI and friends newsletter. PR #9749 by @tiangolo.


### Translations¶
  * 🌐 Add Persian translation for `docs/fa/docs/advanced/sub-applications.md`. PR #9692 by @mojtabapaso.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/response-model.md`. PR #9675 by @glsglsgls.


### Internal¶
  * 🔨 Enable linenums in MkDocs Material during local live development to simplify highlighting code. PR #9769 by @tiangolo.
  * ⬆ Update httpx requirement from <0.24.0,>=0.23.0 to >=0.23.0,<0.25.0. PR #9724 by @dependabot[bot].
  * ⬆ Bump mkdocs-material from 9.1.16 to 9.1.17. PR #9746 by @dependabot[bot].
  * 🔥 Remove missing translation dummy pages, no longer necessary. PR #9751 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #9259 by @pre-commit-ci[bot].
  * ✨ Add Material for MkDocs Insiders features and cards. PR #9748 by @tiangolo.
  * 🔥 Remove languages without translations. PR #9743 by @tiangolo.
  * ✨ Refactor docs for building scripts, use MkDocs hooks, simplify (remove) configs for languages. PR #9742 by @tiangolo.
  * 🔨 Add MkDocs hook that renames sections based on the first index file. PR #9737 by @tiangolo.
  * 👷 Make cron jobs run only on main repo, not on forks, to avoid error notifications from missing tokens. PR #9735 by @tiangolo.
  * 🔧 Update MkDocs for other languages. PR #9734 by @tiangolo.
  * 👷 Refactor Docs CI, run in multiple workers with a dynamic matrix to optimize speed. PR #9732 by @tiangolo.
  * 🔥 Remove old internal GitHub Action watch-previews that is no longer needed. PR #9730 by @tiangolo.
  * ⬆️ Upgrade MkDocs and MkDocs Material. PR #9729 by @tiangolo.
  * 👷 Build and deploy docs only on docs changes. PR #9728 by @tiangolo.


## 0.98.0¶
### Features¶
  * ✨ Allow disabling `redirect_slashes` at the FastAPI app level. PR #3432 by @cyberlis.


### Docs¶
  * 📝 Update docs on Pydantic using ujson internally. PR #5804 by @mvasilkov.
  * ✏ Rewording in `docs/en/docs/tutorial/debugging.md`. PR #9581 by @ivan-abc.
  * 📝 Add german blog post (Domain-driven Design mit Python und FastAPI). PR #9261 by @msander.
  * ✏️ Tweak wording in `docs/en/docs/tutorial/security/index.md`. PR #9561 by @jyothish-mohan.
  * 📝 Update `Annotated` notes in `docs/en/docs/tutorial/schema-extra-example.md`. PR #9620 by @Alexandrhub.
  * ✏️ Fix typo `Annotation` -> `Annotated` in `docs/en/docs/tutorial/query-params-str-validations.md`. PR #9625 by @mccricardo.
  * 📝 Use in memory database for testing SQL in docs. PR #1223 by @HarshaLaxman.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/metadata.md`. PR #9681 by @TabarakoAkula.
  * 🌐 Fix typo in Spanish translation for `docs/es/docs/tutorial/first-steps.md`. PR #9571 by @lilidl-nft.
  * 🌐 Add Russian translation for `docs/tutorial/path-operation-configuration.md`. PR #9696 by @TabarakoAkula.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/security/index.md`. PR #9666 by @lordqyxz.
  * 🌐 Add Chinese translations for `docs/zh/docs/advanced/settings.md`. PR #9652 by @ChoyeonChern.
  * 🌐 Add Chinese translations for `docs/zh/docs/advanced/websockets.md`. PR #9651 by @ChoyeonChern.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/testing.md`. PR #9641 by @wdh99.
  * 🌐 Add Russian translation for `docs/tutorial/extra-models.md`. PR #9619 by @ivan-abc.
  * 🌐 Add Russian translation for `docs/tutorial/cors.md`. PR #9608 by @ivan-abc.
  * 🌐 Add Polish translation for `docs/pl/docs/features.md`. PR #5348 by @mbroton.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/body-nested-models.md`. PR #9605 by @Alexandrhub.


### Internal¶
  * ⬆ Bump ruff from 0.0.272 to 0.0.275. PR #9721 by @dependabot[bot].
  * ⬆ Update uvicorn[standard] requirement from <0.21.0,>=0.12.0 to >=0.12.0,<0.23.0. PR #9463 by @dependabot[bot].
  * ⬆ Bump mypy from 1.3.0 to 1.4.0. PR #9719 by @dependabot[bot].
  * ⬆ Update pre-commit requirement from <3.0.0,>=2.17.0 to >=2.17.0,<4.0.0. PR #9251 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.8.5 to 1.8.6. PR #9482 by @dependabot[bot].
  * ✏️ Fix tooltips for light/dark theme toggler in docs. PR #9588 by @pankaj1707k.
  * 🔧 Set minimal hatchling version needed to build the package. PR #9240 by @mgorny.
  * 📝 Add repo link to PyPI. PR #9559 by @JacobCoffee.
  * ✏️ Fix typos in data for tests. PR #4958 by @ryanrussell.
  * 🔧 Update sponsors, add Flint. PR #9699 by @tiangolo.
  * 👷 Lint in CI only once, only with one version of Python, run tests with all of them. PR #9686 by @tiangolo.


## 0.97.0¶
### Features¶
  * ✨ Add support for `dependencies` in WebSocket routes. PR #4534 by @paulo-raca.
  * ✨ Add exception handler for `WebSocketRequestValidationError` (which also allows to override it). PR #6030 by @kristjanvalur.


### Refactors¶
  * ⬆️ Upgrade and fully migrate to Ruff, remove isort, includes a couple of tweaks suggested by the new version of Ruff. PR #9660 by @tiangolo.
  * ♻️ Update internal type annotations and upgrade mypy. PR #9658 by @tiangolo.
  * ♻️ Simplify `AsyncExitStackMiddleware` as without Python 3.6 `AsyncExitStack` is always available. PR #9657 by @tiangolo.


### Upgrades¶
  * ⬆️ Upgrade Black. PR #9661 by @tiangolo.


### Internal¶
  * 💚 Update CI cache to fix installs when dependencies change. PR #9659 by @tiangolo.
  * ⬇️ Separate requirements for development into their own requirements.txt files, they shouldn't be extras. PR #9655 by @tiangolo.


## 0.96.1¶
### Fixes¶
  * 🐛 Fix `HTTPException` header type annotations. PR #9648 by @tiangolo.
  * 🐛 Fix OpenAPI model fields int validations, `gte` to `ge`. PR #9635 by @tiangolo.


### Upgrades¶
  * 📌 Update minimum version of Pydantic to >=1.7.4. This fixes an issue when trying to use an old version of Pydantic. PR #9567 by @Kludex.


### Refactors¶
  * ♻ Remove `media_type` from `ORJSONResponse` as it's inherited from the parent class. PR #5805 by @Kludex.
  * ♻ Instantiate `HTTPException` only when needed, optimization refactor. PR #5356 by @pawamoy.


### Docs¶
  * 🔥 Remove link to Pydantic's benchmark, as it was removed there. PR #5811 by @Kludex.


### Translations¶
  * 🌐 Fix spelling in Indonesian translation of `docs/id/docs/tutorial/index.md`. PR #5635 by @purwowd.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/index.md`. PR #5896 by @Wilidon.
  * 🌐 Add Chinese translations for `docs/zh/docs/advanced/response-change-status-code.md` and `docs/zh/docs/advanced/response-headers.md`. PR #9544 by @ChoyeonChern.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/schema-extra-example.md`. PR #9621 by @Alexandrhub.


### Internal¶
  * 🔧 Add sponsor Platform.sh. PR #9650 by @tiangolo.
  * 👷 Add custom token to Smokeshow and Preview Docs for download-artifact, to prevent API rate limits. PR #9646 by @tiangolo.
  * 👷 Add custom tokens for GitHub Actions to avoid rate limits. PR #9647 by @tiangolo.


## 0.96.0¶
### Features¶
  * ⚡ Update `create_cloned_field` to use a global cache and improve startup performance. PR #4645 by @madkinsz and previous original PR by @huonw.


### Docs¶
  * 📝 Update Deta deployment tutorial for compatibility with Deta Space. PR #6004 by @mikBighne98.
  * ✏️ Fix typo in Deta deployment tutorial. PR #9501 by @lemonyte.


### Translations¶
  * 🌐 Add Russian translation for `docs/tutorial/body.md`. PR #3885 by @solomein-sv.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/static-files.md`. PR #9580 by @Alexandrhub.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/query-params.md`. PR #9584 by @Alexandrhub.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/first-steps.md`. PR #9471 by @AGolicyn.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/debugging.md`. PR #9579 by @Alexandrhub.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/path-params.md`. PR #9519 by @AGolicyn.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/static-files.md`. PR #9436 by @wdh99.
  * 🌐 Update Spanish translation including new illustrations in `docs/es/docs/async.md`. PR #9483 by @andresbermeoq.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/path-params-numeric-validations.md`. PR #9563 by @ivan-abc.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/concepts.md`. PR #9577 by @Xewus.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/body-multiple-params.md`. PR #9586 by @Alexandrhub.


### Internal¶
  * 👥 Update FastAPI People. PR #9602 by @github-actions[bot].
  * 🔧 Update sponsors, remove InvestSuite. PR #9612 by @tiangolo.


## 0.95.2¶
  * ⬆️ Upgrade Starlette version to `>=0.27.0` for a security release. PR #9541 by @tiangolo. Details on Starlette's security advisory.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/advanced/events.md`. PR #9326 by @oandersonmagalhaes.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/manually.md`. PR #9417 by @Xewus.
  * 🌐 Add setup for translations to Lao. PR #9396 by @TheBrown.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/testing.md`. PR #9403 by @Xewus.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/https.md`. PR #9428 by @Xewus.
  * ✏ Fix command to install requirements in Windows. PR #9445 by @MariiaRomanuik.
  * 🌐 Add French translation for `docs/fr/docs/advanced/response-directly.md`. PR #9415 by @axel584.
  * 🌐 Initiate Czech translation setup. PR #9288 by @3p1463k.
  * ✏ Fix typo in Portuguese docs for `docs/pt/docs/index.md`. PR #9337 by @lucasbalieiro.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/response-status-code.md`. PR #9370 by @nadia3373.


### Internal¶
  * 🐛 Fix `flask.escape` warning for internal tests. PR #9468 by @samuelcolvin.
  * ✅ Refactor 2 tests, for consistency and simplification. PR #9504 by @tiangolo.
  * ✅ Refactor OpenAPI tests, prepare for Pydantic v2. PR #9503 by @tiangolo.
  * ⬆ Bump dawidd6/action-download-artifact from 2.26.0 to 2.27.0. PR #9394 by @dependabot[bot].
  * 💚 Disable setup-python pip cache in CI. PR #9438 by @tiangolo.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.6.4 to 1.8.5. PR #9346 by @dependabot[bot].


## 0.95.1¶
### Fixes¶
  * 🐛 Fix using `Annotated` in routers or path operations decorated multiple times. PR #9315 by @sharonyogev.


### Docs¶
  * 🌐 🔠 📄 🐢 Translate docs to Emoji 🥳 🎉 💥 🤯 🤯. PR #5385 by @LeeeeT.
  * 📝 Add notification message warning about old versions of FastAPI not supporting `Annotated`. PR #9298 by @grdworkin.
  * 📝 Fix typo in `docs/en/docs/advanced/behind-a-proxy.md`. PR #5681 by @Leommjr.
  * ✏ Fix wrong import from typing module in Persian translations for `docs/fa/docs/index.md`. PR #6083 by @Kimiaattaei.
  * ✏️ Fix format, remove unnecessary asterisks in `docs/en/docs/help-fastapi.md`. PR #9249 by @armgabrielyan.
  * ✏ Fix typo in `docs/en/docs/tutorial/query-params-str-validations.md`. PR #9272 by @nicornk.
  * ✏ Fix typo/bug in inline code example in `docs/en/docs/tutorial/query-params-str-validations.md`. PR #9273 by @tim-habitat.
  * ✏ Fix typo in `docs/en/docs/tutorial/path-params-numeric-validations.md`. PR #9282 by @aadarsh977.
  * ✏ Fix typo: 'wll' to 'will' in `docs/en/docs/tutorial/query-params-str-validations.md`. PR #9380 by @dasstyxx.


### Translations¶
  * 🌐 Add French translation for `docs/fr/docs/advanced/index.md`. PR #5673 by @axel584.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/body-nested-models.md`. PR #4053 by @luccasmmg.
  * 🌐 Add Russian translation for `docs/ru/docs/alternatives.md`. PR #5994 by @Xewus.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/extra-models.md`. PR #5912 by @LorhanSohaky.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/path-operation-configuration.md`. PR #5936 by @LorhanSohaky.
  * 🌐 Add Russian translation for `docs/ru/docs/contributing.md`. PR #6002 by @stigsanek.
  * 🌐 Add Korean translation for `docs/tutorial/dependencies/classes-as-dependencies.md`. PR #9176 by @sehwan505.
  * 🌐 Add Russian translation for `docs/ru/docs/project-generation.md`. PR #9243 by @Xewus.
  * 🌐 Add French translation for `docs/fr/docs/index.md`. PR #9265 by @frabc.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/query-params-str-validations.md`. PR #9267 by @dedkot01.
  * 🌐 Add Russian translation for `docs/ru/docs/benchmarks.md`. PR #9271 by @Xewus.


### Internal¶
  * 🔧 Update sponsors: remove Jina. PR #9388 by @tiangolo.
  * 🔧 Update sponsors, add databento, remove Ines's course and StriveWorks. PR #9351 by @tiangolo.


## 0.95.0¶
### Highlights¶
This release adds support for dependencies and parameters using `Annotated` and recommends its usage. ✨
This has **several benefits** , one of the main ones is that now the parameters of your functions with `Annotated` would **not be affected** at all.
If you call those functions in **other places in your code** , the actual **default values** will be kept, your editor will help you notice missing **required arguments** , Python will require you to pass required arguments at **runtime** , you will be able to **use the same functions** for different things and with different libraries (e.g. **Typer** will soon support `Annotated` too, then you could use the same function for an API and a CLI), etc.
Because `Annotated` is **standard Python** , you still get all the **benefits** from editors and tools, like **autocompletion** , **inline errors** , etc.
One of the **biggest benefits** is that now you can create `Annotated` dependencies that are then shared by multiple _path operation functions_ , this will allow you to **reduce** a lot of **code duplication** in your codebase, while keeping all the support from editors and tools.
For example, you could have code like this:
```
defget_current_user(token: str):
  # authenticate user
  return User()
@app.get("/items/")
defread_items(user: User = Depends(get_current_user)):
  ...
@app.post("/items/")
defcreate_item(*, user: User = Depends(get_current_user), item: Item):
  ...
@app.get("/items/{item_id}")
defread_item(*, user: User = Depends(get_current_user), item_id: int):
  ...
@app.delete("/items/{item_id}")
defdelete_item(*, user: User = Depends(get_current_user), item_id: int):
  ...

```

There's a bit of code duplication for the dependency:
```
user: User = Depends(get_current_user)

```

...the bigger the codebase, the more noticeable it is.
Now you can create an annotated dependency once, like this:
```
CurrentUser = Annotated[User, Depends(get_current_user)]

```

And then you can reuse this `Annotated` dependency:
```
CurrentUser = Annotated[User, Depends(get_current_user)]
@app.get("/items/")
defread_items(user: CurrentUser):
  ...
@app.post("/items/")
defcreate_item(user: CurrentUser, item: Item):
  ...
@app.get("/items/{item_id}")
defread_item(user: CurrentUser, item_id: int):
  ...
@app.delete("/items/{item_id}")
defdelete_item(user: CurrentUser, item_id: int):
  ...

```

...and `CurrentUser` has all the typing information as `User`, so your editor will work as expected (autocompletion and everything), and **FastAPI** will be able to understand the dependency defined in `Annotated`. 😎
Roughly **all the docs** have been rewritten to use `Annotated` as the main way to declare **parameters** and **dependencies**. All the **examples** in the docs now include a version with `Annotated` and a version without it, for each of the specific Python versions (when there are small differences/improvements in more recent versions). There were around 23K new lines added between docs, examples, and tests. 🚀
The key updated docs are:
  * Python Types Intro:
    * Type Hints with Metadata Annotations.
  * Tutorial:
    * Query Parameters and String Validations - Additional validation
      * Advantages of `Annotated`
    * Path Parameters and Numeric Validations - Order the parameters as you need, tricks
      * Better with `Annotated`
    * Dependencies - First Steps - Share `Annotated` dependencies


Special thanks to @nzig for the core implementation and to @adriangb for the inspiration and idea with Xpresso! 🚀
### Features¶
  * ✨Add support for PEP-593 `Annotated` for specifying dependencies and parameters. PR #4871 by @nzig.


### Docs¶
  * 📝 Tweak tip recommending `Annotated` in docs. PR #9270 by @tiangolo.
  * 📝 Update order of examples, latest Python version first, and simplify version tab names. PR #9269 by @tiangolo.
  * 📝 Update all docs to use `Annotated` as the main recommendation, with new examples and tests. PR #9268 by @tiangolo.


## 0.94.1¶
### Fixes¶
  * 🎨 Fix types for lifespan, upgrade Starlette to 0.26.1. PR #9245 by @tiangolo.


## 0.94.0¶
### Upgrades¶
  * ⬆ Upgrade python-multipart to support 0.0.6. PR #9212 by @musicinmybrain.
  * ⬆️ Upgrade Starlette version, support new `lifespan` with state. PR #9239 by @tiangolo.


### Docs¶
  * 📝 Update Sentry link in docs. PR #9218 by @smeubank.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/history-design-future.md`. PR #5986 by @Xewus.


### Internal¶
  * ➕ Add `pydantic` to PyPI classifiers. PR #5914 by @yezz123.
  * ⬆ Bump black from 22.10.0 to 23.1.0. PR #5953 by @dependabot[bot].
  * ⬆ Bump types-ujson from 5.6.0.0 to 5.7.0.1. PR #6027 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.24.3 to 2.26.0. PR #6034 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5709 by @pre-commit-ci[bot].


## 0.93.0¶
### Features¶
  * ✨ Add support for `lifespan` async context managers (superseding `startup` and `shutdown` events). Initial PR #2944 by @uSpike.


Now, instead of using independent `startup` and `shutdown` events, you can define that logic in a single function with `yield` decorated with `@asynccontextmanager` (an async context manager).
For example:
```
fromcontextlibimport asynccontextmanager
fromfastapiimport FastAPI
deffake_answer_to_everything_ml_model(x: float):
  return x * 42
ml_models = {}
@asynccontextmanager
async deflifespan(app: FastAPI):
  # Load the ML model
  ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
  yield
  # Clean up the ML models and release the resources
  ml_models.clear()
app = FastAPI(lifespan=lifespan)
@app.get("/predict")
async defpredict(x: float):
  result = ml_models["answer_to_everything"](x)
  return {"result": result}

```

**Note** : This is the recommended way going forward, instead of using `startup` and `shutdown` events.
Read more about it in the new docs: Advanced User Guide: Lifespan Events.
### Docs¶
  * ✏ Fix formatting in `docs/en/docs/tutorial/metadata.md` for `ReDoc`. PR #6005 by @eykamp.


### Translations¶
  * 🌐 Tamil translations - initial setup. PR #5564 by @gusty1g.
  * 🌐 Add French translation for `docs/fr/docs/advanced/path-operation-advanced-configuration.md`. PR #9221 by @axel584.
  * 🌐 Add French translation for `docs/tutorial/debugging.md`. PR #9175 by @frabc.
  * 🌐 Initiate Armenian translation setup. PR #5844 by @har8.
  * 🌐 Add French translation for `deployment/manually.md`. PR #3693 by @rjNemo.


### Internal¶
  * 👷 Update translation bot messages. PR #9206 by @tiangolo.
  * 👷 Update translations bot to use Discussions, and notify when a PR is done. PR #9183 by @tiangolo.
  * 🔧 Update sponsors-badges. PR #9182 by @tiangolo.
  * 👥 Update FastAPI People. PR #9181 by @github-actions[bot].
  * 🔊 Log GraphQL errors in FastAPI People, because it returns 200, with a payload with an error. PR #9171 by @tiangolo.
  * 💚 Fix/workaround GitHub Actions in Docker with git for FastAPI People. PR #9169 by @tiangolo.
  * ♻️ Refactor FastAPI Experts to use only discussions now that questions are migrated. PR #9165 by @tiangolo.
  * ⬆️ Upgrade analytics. PR #6025 by @tiangolo.
  * ⬆️ Upgrade and re-enable installing Typer-CLI. PR #6008 by @tiangolo.


## 0.92.0¶
🚨 This is a security fix. Please upgrade as soon as possible.
### Upgrades¶
  * ⬆️ Upgrade Starlette to 0.25.0. PR #5996 by @tiangolo.
    * This solves a vulnerability that could allow denial of service attacks by using many small multipart fields/files (parts), consuming high CPU and memory.
    * Only applications using forms (e.g. file uploads) could be affected.
    * For most cases, upgrading won't have any breaking changes.


## 0.91.0¶
### Upgrades¶
  * ⬆️ Upgrade Starlette version to `0.24.0` and refactor internals for compatibility. PR #5985 by @tiangolo.
    * This can solve nuanced errors when using middlewares. Before Starlette `0.24.0`, a new instance of each middleware class would be created when a new middleware was added. That normally was not a problem, unless the middleware class expected to be created only once, with only one instance, that happened in some cases. This upgrade would solve those cases (thanks @adriangb! Starlette PR #2017). Now the middleware class instances are created once, right before the first request (the first time the app is called).
    * If you depended on that previous behavior, you might need to update your code. As always, make sure your tests pass before merging the upgrade.


## 0.90.1¶
### Upgrades¶
  * ⬆️ Upgrade Starlette range to allow 0.23.1. PR #5980 by @tiangolo.


### Docs¶
  * ✏ Tweak wording to clarify `docs/en/docs/project-generation.md`. PR #5930 by @chandra-deb.
  * ✏ Update Pydantic GitHub URLs. PR #5952 by @yezz123.
  * 📝 Add opinion from Cisco. PR #5981 by @tiangolo.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/cookie-params.md`. PR #5890 by @bnzone.


### Internal¶
  * ✏ Update `zip-docs.sh` internal script, remove extra space. PR #5931 by @JuanPerdomo00.


## 0.90.0¶
### Upgrades¶
  * ⬆️ Bump Starlette from 0.22.0 to 0.23.0. Initial PR #5739 by @Kludex.


### Docs¶
  * 📝 Add article "Tortoise ORM / FastAPI 整合快速筆記" to External Links. PR #5496 by @Leon0824.
  * 👥 Update FastAPI People. PR #5954 by @github-actions[bot].
  * 📝 Micro-tweak help docs. PR #5960 by @tiangolo.
  * 🔧 Update new issue chooser to direct to GitHub Discussions. PR #5948 by @tiangolo.
  * 📝 Recommend GitHub Discussions for questions. PR #5944 by @tiangolo.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/body-fields.md`. PR #5898 by @simatheone.
  * 🌐 Add Russian translation for `docs/ru/docs/help-fastapi.md`. PR #5970 by @tiangolo.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/static-files.md`. PR #5858 by @batlopes.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/encoder.md`. PR #5525 by @felipebpl.
  * 🌐 Add Russian translation for `docs/ru/docs/contributing.md`. PR #5870 by @Xewus.


### Internal¶
  * ⬆️ Upgrade Ubuntu version for docs workflow. PR #5971 by @tiangolo.
  * 🔧 Update sponsors badges. PR #5943 by @tiangolo.
  * ✨ Compute FastAPI Experts including GitHub Discussions. PR #5941 by @tiangolo.
  * ⬆️ Upgrade isort and update pre-commit. PR #5940 by @tiangolo.
  * 🔧 Add template for questions in Discussions. PR #5920 by @tiangolo.
  * 🔧 Update Sponsor Budget Insight to Powens. PR #5916 by @tiangolo.
  * 🔧 Update GitHub Sponsors badge data. PR #5915 by @tiangolo.


## 0.89.1¶
### Fixes¶
  * 🐛 Ignore Response classes on return annotation. PR #5855 by @Kludex. See the new docs in the PR below.


### Docs¶
  * 📝 Update docs and examples for Response Model with Return Type Annotations, and update runtime error. PR #5873 by @tiangolo. New docs at Response Model - Return Type: Other Return Type Annotations.
  * 📝 Add External Link: FastAPI lambda container: serverless simplified. PR #5784 by @rafrasenberg.


### Translations¶
  * 🌐 Add Turkish translation for `docs/tr/docs/tutorial/first_steps.md`. PR #5691 by @Kadermiyanyedi.


## 0.89.0¶
### Features¶
  * ✨ Add support for function return type annotations to declare the `response_model`. Initial PR #1436 by @uriyyo.


Now you can declare the return type / `response_model` in the function return type annotation:
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
@app.get("/items/")
async defread_items() -> list[Item]:
  return [
    Item(name="Portal Gun", price=42.0),
    Item(name="Plumbus", price=32.0),
  ]

```

FastAPI will use the return type annotation to perform:
  * Data validation
  * Automatic documentation
    * It could power automatic client generators
  * **Data filtering**


Before this version it was only supported via the `response_model` parameter.
Read more about it in the new docs: Response Model - Return Type.
### Docs¶
  * 📝 Add External Link: Authorization on FastAPI with Casbin. PR #5712 by @Xhy-5000.
  * ✏ Fix typo in `docs/en/docs/async.md`. PR #5785 by @Kingdageek.
  * ✏ Fix typo in `docs/en/docs/deployment/concepts.md`. PR #5824 by @kelbyfaessler.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/fastapi-people.md`. PR #5577 by @Xewus.
  * 🌐 Fix typo in Chinese translation for `docs/zh/docs/benchmarks.md`. PR #4269 by @15027668g.
  * 🌐 Add Korean translation for `docs/tutorial/cors.md`. PR #3764 by @NinaHwang.


### Internal¶
  * ⬆ Update coverage[toml] requirement from <7.0,>=6.5.0 to >=6.5.0,<8.0. PR #5801 by @dependabot[bot].
  * ⬆ Update uvicorn[standard] requirement from <0.19.0,>=0.12.0 to >=0.12.0,<0.21.0 for development. PR #5795 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.24.2 to 2.24.3. PR #5842 by @dependabot[bot].
  * 👥 Update FastAPI People. PR #5825 by @github-actions[bot].
  * ⬆ Bump types-ujson from 5.5.0 to 5.6.0.0. PR #5735 by @dependabot[bot].
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.5.2 to 1.6.4. PR #5750 by @dependabot[bot].
  * 👷 Add GitHub Action gate/check. PR #5492 by @webknjaz.
  * 🔧 Update sponsors, add Svix. PR #5848 by @tiangolo.
  * 🔧 Remove Doist sponsor. PR #5847 by @tiangolo.
  * ⬆ Update sqlalchemy requirement from <=1.4.41,>=1.3.18 to >=1.3.18,<1.4.43. PR #5540 by @dependabot[bot].
  * ⬆ Bump nwtgck/actions-netlify from 1.2.4 to 2.0.0. PR #5757 by @dependabot[bot].
  * 👷 Refactor CI artifact upload/download for docs previews. PR #5793 by @tiangolo.
  * ⬆ Bump pypa/gh-action-pypi-publish from 1.5.1 to 1.5.2. PR #5714 by @dependabot[bot].
  * 👥 Update FastAPI People. PR #5722 by @github-actions[bot].
  * 🔧 Update sponsors, disable course bundle. PR #5713 by @tiangolo.
  * ⬆ Update typer[all] requirement from <0.7.0,>=0.6.1 to >=0.6.1,<0.8.0. PR #5639 by @dependabot[bot].


## 0.88.0¶
### Upgrades¶
  * ⬆ Bump Starlette to version `0.22.0` to fix bad encoding for query parameters in new `TestClient`. PR #5659 by @azogue.


### Docs¶
  * ✏️ Fix typo in docs for `docs/en/docs/advanced/middleware.md`. PR #5376 by @rifatrakib.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/deployment/docker.md`. PR #5663 by @ayr-ton.


### Internal¶
  * 👷 Tweak build-docs to improve CI performance. PR #5699 by @tiangolo.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5566 by @pre-commit-ci[bot].
  * ⬆️ Upgrade Ruff. PR #5698 by @tiangolo.
  * 👷 Remove pip cache for Smokeshow as it depends on a requirements.txt. PR #5700 by @tiangolo.
  * 💚 Fix pip cache for Smokeshow. PR #5697 by @tiangolo.
  * 👷 Fix and tweak CI cache handling. PR #5696 by @tiangolo.
  * 👷 Update `setup-python` action in tests to use new caching feature. PR #5680 by @madkinsz.
  * ⬆ Bump black from 22.8.0 to 22.10.0. PR #5569 by @dependabot[bot].


## 0.87.0¶
Highlights of this release:
  * Upgraded Starlette
    * Now the `TestClient` is based on HTTPX instead of Requests. 🚀
    * There are some possible **breaking changes** in the `TestClient` usage, but @Kludex built bump-testclient to help you automatize migrating your tests. Make sure you are using Git and that you can undo any unnecessary changes (false positive changes, etc) before using `bump-testclient`.
  * New WebSocketException (and docs), re-exported from Starlette.
  * Upgraded and relaxed dependencies for package extras `all` (including new Uvicorn version), when you install `"fastapi[all]"`.
  * New docs about how to **Help Maintain FastAPI**.


### Features¶
  * ⬆️ Upgrade and relax dependencies for extras "all". PR #5634 by @tiangolo.
  * ✨ Re-export Starlette's `WebSocketException` and add it to docs. PR #5629 by @tiangolo.
  * 📝 Update references to Requests for tests to HTTPX, and add HTTPX to extras. PR #5628 by @tiangolo.
  * ⬆ Upgrade Starlette to `0.21.0`, including the new `TestClient` based on HTTPX. PR #5471 by @pawelrubin.


### Docs¶
  * ✏️ Tweak Help FastAPI from PR review after merging. PR #5633 by @tiangolo.
  * ✏️ Clarify docs on CORS. PR #5627 by @paxcodes.
  * 📝 Update Help FastAPI: Help Maintain FastAPI. PR #5632 by @tiangolo.


### Translations¶
  * 🌐 Fix highlight lines for Japanese translation for `docs/tutorial/query-params.md`. PR #2969 by @ftnext.
  * 🌐 Add French translation for `docs/fr/docs/advanced/additional-status-code.md`. PR #5477 by @axel584.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/request-forms-and-files.md`. PR #5579 by @batlopes.
  * 🌐 Add Japanese translation for `docs/ja/docs/advanced/websockets.md`. PR #4983 by @xryuseix.


### Internal¶
  * ✨ Use Ruff for linting. PR #5630 by @tiangolo.
  * 🛠 Add Arabic issue number to Notify Translations GitHub Action. PR #5610 by @tiangolo.
  * ⬆ Bump dawidd6/action-download-artifact from 2.24.1 to 2.24.2. PR #5609 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.24.0 to 2.24.1. PR #5603 by @dependabot[bot].
  * 📝 Update coverage badge to use Samuel Colvin's Smokeshow. PR #5585 by @tiangolo.


## 0.86.0¶
### Features¶
  * ⬆ Add Python 3.11 to the officially supported versions. PR #5587 by @tiangolo.
  * ✅ Enable tests for Python 3.11. PR #4881 by @tiangolo.


### Fixes¶
  * 🐛 Close FormData (uploaded files) after the request is done. PR #5465 by @adriangb.


### Docs¶
  * ✏ Fix typo in `docs/en/docs/tutorial/security/oauth2-jwt.md`. PR #5584 by @vivekashok1221.


### Translations¶
  * 🌐 Update wording in Chinese translation for `docs/zh/docs/python-types.md`. PR #5416 by @supercaizehua.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/index.md`. PR #5336 by @Xewus.
  * 🌐 Update Chinese translation for `docs/tutorial/security/oauth2-jwt.md`. PR #3846 by @jaystone776.


### Internal¶
  * 👷 Update FastAPI People to exclude bots: pre-commit-ci, dependabot. PR #5586 by @tiangolo.
  * 🎨 Format OpenAPI JSON in `test_starlette_exception.py`. PR #5379 by @iudeen.
  * 👷 Switch from Codecov to Smokeshow plus pytest-cov to pure coverage for internal tests. PR #5583 by @tiangolo.
  * 👥 Update FastAPI People. PR #5571 by @github-actions[bot].


## 0.85.2¶
### Docs¶
  * ✏ Fix grammar and add helpful links to dependencies in `docs/en/docs/async.md`. PR #5432 by @pamelafox.
  * ✏ Fix broken link in `alternatives.md`. PR #5455 by @su-shubham.
  * ✏ Fix typo in docs about contributing, for compatibility with `pip` in Zsh. PR #5523 by @zhangbo2012.
  * 📝 Fix typo in docs with examples for Python 3.10 instead of 3.9. PR #5545 by @feliciss.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/request-forms.md`. PR #4934 by @batlopes.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/dependencies/classes-as-dependencies.md`. PR #4971 by @Zssaer.
  * 🌐 Add French translation for `deployment/deta.md`. PR #3692 by @rjNemo.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/query-params-str-validations.md`. PR #5255 by @hjlarry.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/sql-databases.md`. PR #4999 by @Zssaer.
  * 🌐 Add Chinese translation for `docs/zh/docs/advanced/wsgi.md`. PR #4505 by @ASpathfinder.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/body-multiple-params.md`. PR #4111 by @lbmendes.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/path-params-numeric-validations.md`. PR #4099 by @lbmendes.
  * 🌐 Add French translation for `deployment/versions.md`. PR #3690 by @rjNemo.
  * 🌐 Add French translation for `docs/fr/docs/help-fastapi.md`. PR #2233 by @JulianMaurin.
  * 🌐 Fix typo in Chinese translation for `docs/zh/docs/tutorial/security/first-steps.md`. PR #5530 by @yuki1sntSnow.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/response-status-code.md`. PR #4922 by @batlopes.
  * 🔧 Add config for Tamil translations. PR #5563 by @tiangolo.


### Internal¶
  * ⬆ Bump internal dependency mypy from 0.971 to 0.982. PR #5541 by @dependabot[bot].
  * ⬆ Bump nwtgck/actions-netlify from 1.2.3 to 1.2.4. PR #5507 by @dependabot[bot].
  * ⬆ Bump internal dependency types-ujson from 5.4.0 to 5.5.0. PR #5537 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.23.0 to 2.24.0. PR #5508 by @dependabot[bot].
  * ⬆ Update internal dependency pytest-cov requirement from <4.0.0,>=2.12.0 to >=2.12.0,<5.0.0. PR #5539 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5536 by @pre-commit-ci[bot].
  * 🐛 Fix internal Trio test warnings. PR #5547 by @samuelcolvin.
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5408 by @pre-commit-ci[bot].
  * ⬆️ Upgrade Typer to include Rich in scripts for docs. PR #5502 by @tiangolo.
  * 🐛 Fix calling `mkdocs` for languages as a subprocess to fix/enable MkDocs Material search plugin. PR #5501 by @tiangolo.


## 0.85.1¶
### Fixes¶
  * 🐛 Fix support for strings in OpenAPI status codes: `default`, `1XX`, `2XX`, `3XX`, `4XX`, `5XX`. PR #5187 by @JarroVGIT.


### Docs¶
  * 📝 Add WayScript x FastAPI Tutorial to External Links section. PR #5407 by @moneeka.


### Internal¶
  * 👥 Update FastAPI People. PR #5447 by @github-actions[bot].
  * 🔧 Disable Material for MkDocs search plugin. PR #5495 by @tiangolo.
  * 🔇 Ignore Trio warning in tests for CI. PR #5483 by @samuelcolvin.


## 0.85.0¶
### Features¶
  * ⬆ Upgrade version required of Starlette from `0.19.1` to `0.20.4`. Initial PR #4820 by @Kludex.
    * This includes several bug fixes in Starlette.
  * ⬆️ Upgrade Uvicorn max version in public extras: all. From `>=0.12.0,<0.18.0` to `>=0.12.0,<0.19.0`. PR #5401 by @tiangolo.


### Internal¶
  * ⬆️ Upgrade dependencies for doc and dev internal extras: Typer, Uvicorn. PR #5400 by @tiangolo.
  * ⬆️ Upgrade test dependencies: Black, HTTPX, databases, types-ujson. PR #5399 by @tiangolo.
  * ⬆️ Upgrade mypy and tweak internal type annotations. PR #5398 by @tiangolo.
  * 🔧 Update test dependencies, upgrade Pytest, move dependencies from dev to test. PR #5396 by @tiangolo.


## 0.84.0¶
### Breaking Changes¶
This version of FastAPI drops support for Python 3.6. 🔥 Please upgrade to a supported version of Python (3.7 or above), Python 3.6 reached the end-of-life a long time ago. 😅☠
  * 🔧 Update package metadata, drop support for Python 3.6, move build internals from Flit to Hatch. PR #5240 by @ofek.


## 0.83.0¶
🚨 This is probably the last release (or one of the last releases) to support Python 3.6. 🔥
Python 3.6 reached the end-of-life and is no longer supported by Python since around a year ago.
You hopefully updated to a supported version of Python a while ago. If you haven't, you really should.
### Features¶
  * ✨ Add support in `jsonable_encoder` for include and exclude with dataclasses. PR #4923 by @DCsunset.


### Fixes¶
  * 🐛 Fix `RuntimeError` raised when `HTTPException` has a status code with no content. PR #5365 by @iudeen.
  * 🐛 Fix empty reponse body when default `status_code` is empty but the a `Response` parameter with `response.status_code` is set. PR #5360 by @tmeckel.


### Docs¶
  * 📝 Update `SECURITY.md`. PR #5377 by @Kludex.


### Internal¶
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5352 by @pre-commit-ci[bot].


## 0.82.0¶
🚨 This is probably the last release (or one of the last releases) to support Python 3.6. 🔥
Python 3.6 reached the end-of-life and is no longer supported by Python since around a year ago.
You hopefully updated to a supported version of Python a while ago. If you haven't, you really should.
### Features¶
  * ✨ Export `WebSocketState` in `fastapi.websockets`. PR #4376 by @matiuszka.
  * ✨ Support Python internal description on Pydantic model's docstring. PR #3032 by @Kludex.
  * ✨ Update `ORJSONResponse` to support non `str` keys and serializing Numpy arrays. PR #3892 by @baby5.


### Fixes¶
  * 🐛 Allow exit code for dependencies with `yield` to always execute, by removing capacity limiter for them, to e.g. allow closing DB connections without deadlocks. PR #5122 by @adriangb.
  * 🐛 Fix FastAPI People GitHub Action: set HTTPX timeout for GraphQL query request. PR #5222 by @iudeen.
  * 🐛 Make sure a parameter defined as required is kept required in OpenAPI even if defined as optional in another dependency. PR #4319 by @cd17822.
  * 🐛 Fix support for path parameters in WebSockets. PR #3879 by @davidbrochart.


### Docs¶
  * ✏ Update Hypercorn link, now pointing to GitHub. PR #5346 by @baconfield.
  * ✏ Tweak wording in `docs/en/docs/advanced/dataclasses.md`. PR #3698 by @pfackeldey.
  * 📝 Add note about Python 3.10 `X | Y` operator in explanation about Response Models. PR #5307 by @MendyLanda.
  * 📝 Add link to New Relic article: "How to monitor FastAPI application performance using Python agent". PR #5260 by @sjyothi54.
  * 📝 Update docs for `ORJSONResponse` with details about improving performance. PR #2615 by @falkben.
  * 📝 Add docs for creating a custom Response class. PR #5331 by @tiangolo.
  * 📝 Add tip about using alias for form data fields. PR #5329 by @tiangolo.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/features.md`. PR #5315 by @Xewus.
  * 🌐 Update Chinese translation for `docs/zh/docs/tutorial/request-files.md`. PR #4529 by @ASpathfinder.
  * 🌐 Add Chinese translation for `docs/zh/docs/tutorial/encoder.md`. PR #4969 by @Zssaer.
  * 🌐 Fix MkDocs file line for Portuguese translation of `background-task.md`. PR #5242 by @ComicShrimp.


### Internal¶
  * 👥 Update FastAPI People. PR #5347 by @github-actions[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.22.0 to 2.23.0. PR #5321 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5318 by @pre-commit-ci[bot].
  * ✏ Fix a small code highlight line error. PR #5256 by @hjlarry.
  * ♻ Internal small refactor, move `operation_id` parameter position in delete method for consistency with the code. PR #4474 by @hiel.
  * 🔧 Update sponsors, disable ImgWhale. PR #5338 by @tiangolo.


## 0.81.0¶
### Features¶
  * ✨ Add ReDoc `<noscript>` warning when JS is disabled. PR #5074 by @evroon.
  * ✨ Add support for `FrozenSet` in parameters (e.g. query). PR #2938 by @juntatalor.
  * ✨ Allow custom middlewares to raise `HTTPException`s and propagate them. PR #2036 by @ghandic.
  * ✨ Preserve `json.JSONDecodeError` information when handling invalid JSON in request body, to support custom exception handlers that use its information. PR #4057 by @UKnowWhoIm.


### Fixes¶
  * 🐛 Fix `jsonable_encoder` for dataclasses with pydantic-compatible fields. PR #3607 by @himbeles.
  * 🐛 Fix support for extending `openapi_extras` with parameter lists. PR #4267 by @orilevari.


### Docs¶
  * ✏ Fix a simple typo in `docs/en/docs/python-types.md`. PR #5193 by @GlitchingCore.
  * ✏ Fix typos in `tests/test_schema_extra_examples.py`. PR #5126 by @supraaxdd.
  * ✏ Fix typos in `docs/en/docs/tutorial/path-params-numeric-validations.md`. PR #5142 by @invisibleroads.
  * 📝 Add step about upgrading pip in the venv to avoid errors when installing dependencies `docs/en/docs/contributing.md`. PR #5181 by @edisnake.
  * ✏ Reword and clarify text in tutorial `docs/en/docs/tutorial/body-nested-models.md`. PR #5169 by @papb.
  * ✏ Fix minor typo in `docs/en/docs/features.md`. PR #5206 by @OtherBarry.
  * ✏ Fix minor typos in `docs/en/docs/async.md`. PR #5125 by @Ksenofanex.
  * 📝 Add external link to docs: "Fastapi, Docker(Docker compose) and Postgres". PR #5033 by @krishnardt.
  * 📝 Simplify example for docs for Additional Responses, remove unnecessary `else`. PR #4693 by @adriangb.
  * 📝 Update docs, compare enums with identity instead of equality. PR #4905 by @MicaelJarniac.
  * ✏ Fix typo in `docs/en/docs/python-types.md`. PR #4886 by @MicaelJarniac.
  * 🎨 Fix syntax highlighting in docs for OpenAPI Callbacks. PR #4368 by @xncbf.
  * ✏ Reword confusing sentence in docs file `typo-fix-path-params-numeric-validations.md`. PR #3219 by @ccrenfroe.
  * 📝 Update docs for handling HTTP Basic Auth with `secrets.compare_digest()` to account for non-ASCII characters. PR #3536 by @lewoudar.
  * 📝 Update docs for testing, fix examples with relative imports. PR #5302 by @tiangolo.


### Translations¶
  * 🌐 Add Russian translation for `docs/ru/docs/index.md`. PR #5289 by @impocode.
  * 🌐 Add Russian translation for `docs/ru/docs/deployment/versions.md`. PR #4985 by @emp7yhead.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/header-params.md`. PR #4921 by @batlopes.
  * 🌐 Update `ko/mkdocs.yml` for a missing link. PR #5020 by @dalinaum.


### Internal¶
  * ⬆ Bump dawidd6/action-download-artifact from 2.21.1 to 2.22.0. PR #5258 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5196 by @pre-commit-ci[bot].
  * 🔥 Delete duplicated tests in `tests/test_tutorial/test_sql_databases/test_sql_databases.py`. PR #5040 by @raccoonyy.
  * ♻ Simplify internal RegEx in `fastapi/utils.py`. PR #5057 by @pylounge.
  * 🔧 Fix Type hint of `auto_error` which does not need to be `Optional[bool]`. PR #4933 by @DavidKimDY.
  * 🔧 Update mypy config, use `strict = true` instead of manual configs. PR #4605 by @michaeloliverx.
  * ♻ Change a `dict()` for `{}` in `fastapi/utils.py`. PR #3138 by @ShahriyarR.
  * ♻ Move internal variable for errors in `jsonable_encoder` to put related code closer. PR #4560 by @GuilleQP.
  * ♻ Simplify conditional assignment in `fastapi/dependencies/utils.py`. PR #4597 by @cikay.
  * ⬆ Upgrade version pin accepted for Flake8, for internal code, to `flake8 >=3.8.3,<6.0.0`. PR #4097 by @jamescurtin.
  * 🍱 Update Jina banner, fix typo. PR #5301 by @tiangolo.


## 0.80.0¶
### Breaking Changes - Fixes¶
  * 🐛 Fix `response_model` not invalidating `None`. PR #2725 by @hukkin.


If you are using `response_model` with some type that doesn't include `None` but the function is returning `None`, it will now raise an internal server error, because you are returning invalid data that violates the contract in `response_model`. Before this release it would allow breaking that contract returning `None`.
For example, if you have an app like this:
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  price: Optional[float] = None
  owner_ids: Optional[List[int]] = None
app = FastAPI()
@app.get("/items/invalidnone", response_model=Item)
defget_invalid_none():
  return None

```

...calling the path `/items/invalidnone` will raise an error, because `None` is not a valid type for the `response_model` declared with `Item`.
You could also be implicitly returning `None` without realizing, for example:
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  price: Optional[float] = None
  owner_ids: Optional[List[int]] = None
app = FastAPI()
@app.get("/items/invalidnone", response_model=Item)
defget_invalid_none():
  if flag:
    return {"name": "foo"}
  # if flag is False, at this point the function will implicitly return None

```

If you have _path operations_ using `response_model` that need to be allowed to return `None`, make it explicit in `response_model` using `Union[Something, None]`:
```
fromtypingimport Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  price: Optional[float] = None
  owner_ids: Optional[List[int]] = None
app = FastAPI()
@app.get("/items/invalidnone", response_model=Union[Item, None])
defget_invalid_none():
  return None

```

This way the data will be correctly validated, you won't have an internal server error, and the documentation will also reflect that this _path operation_ could return `None` (or `null` in JSON).
### Fixes¶
  * ⬆ Upgrade Swagger UI copy of `oauth2-redirect.html` to include fixes for flavors of authorization code flows in Swagger UI. PR #3439 initial PR by @koonpeng.
  * ♻ Strip empty whitespace from description extracted from docstrings. PR #2821 by @and-semakin.
  * 🐛 Fix cached dependencies when using a dependency in `Security()` and other places (e.g. `Depends()`) with different OAuth2 scopes. PR #2945 by @laggardkernel.
  * 🎨 Update type annotations for `response_model`, allow things like `Union[str, None]`. PR #5294 by @tiangolo.


### Translations¶
  * 🌐 Fix typos in German translation for `docs/de/docs/features.md`. PR #4533 by @0xflotus.
  * 🌐 Add missing navigator for `encoder.md` in Korean translation. PR #5238 by @joonas-yoon.
  * (Empty PR merge by accident) #4913.


## 0.79.1¶
### Fixes¶
  * 🐛 Fix `jsonable_encoder` using `include` and `exclude` parameters for non-Pydantic objects. PR #2606 by @xaviml.
  * 🐛 Fix edge case with repeated aliases names not shown in OpenAPI. PR #2351 by @klaa97.
  * 📝 Add misc dependency installs to tutorial docs. PR #2126 by @TeoZosa.


### Docs¶
  * 📝 Add note giving credit for illustrations to Ketrina Thompson. PR #5284 by @tiangolo.
  * ✏ Fix typo in `python-types.md`. PR #5116 by @Kludex.
  * ✏ Fix typo in `docs/en/docs/python-types.md`. PR #5007 by @atiabbz.
  * 📝 Remove unneeded Django/Flask references from async topic intro. PR #5280 by @carltongibson.
  * ✨ Add illustrations for Concurrent burgers and Parallel burgers. PR #5277 by @tiangolo. Updated docs at: Concurrency and Burgers.


### Translations¶
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/query-params.md`. PR #4775 by @batlopes.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/security/first-steps.md`. PR #4954 by @FLAIR7.
  * 🌐 Add translation for `docs/zh/docs/advanced/response-cookies.md`. PR #4638 by @zhangbo2012.
  * 🌐 Add French translation for `docs/fr/docs/deployment/index.md`. PR #3689 by @rjNemo.
  * 🌐 Add Portuguese translation for `tutorial/handling-errors.md`. PR #4769 by @frnsimoes.
  * 🌐 Add French translation for `docs/fr/docs/history-design-future.md`. PR #3451 by @rjNemo.
  * 🌐 Add Russian translation for `docs/ru/docs/tutorial/background-tasks.md`. PR #4854 by @AdmiralDesu.
  * 🌐 Add Chinese translation for `docs/tutorial/security/first-steps.md`. PR #3841 by @jaystone776.
  * 🌐 Add Japanese translation for `docs/ja/docs/advanced/nosql-databases.md`. PR #4205 by @sUeharaE4.
  * 🌐 Add Indonesian translation for `docs/id/docs/tutorial/index.md`. PR #4705 by @bas-baskara.
  * 🌐 Add Persian translation for `docs/fa/docs/index.md` and tweak right-to-left CSS. PR #2395 by @mohsen-mahmoodi.


### Internal¶
  * 🔧 Update Jina sponsorship. PR #5283 by @tiangolo.
  * 🔧 Update Jina sponsorship. PR #5272 by @tiangolo.
  * 🔧 Update sponsors, Striveworks badge. PR #5179 by @tiangolo.


## 0.79.0¶
### Fixes - Breaking Changes¶
  * 🐛 Fix removing body from status codes that do not support it. PR #5145 by @tiangolo.
    * Setting `status_code` to `204`, `304`, or any code below `200` (1xx) will remove the body from the response.
    * This fixes an error in Uvicorn that otherwise would be thrown: `RuntimeError: Response content longer than Content-Length`.
    * This removes `fastapi.openapi.constants.STATUS_CODES_WITH_NO_BODY`, it is replaced by a function in utils.


### Translations¶
  * 🌐 Start of Hebrew translation. PR #5050 by @itay-raveh.
  * 🔧 Add config for Swedish translations notification. PR #5147 by @tiangolo.
  * 🌐 Start of Swedish translation. PR #5062 by @MrRawbin.
  * 🌐 Add Japanese translation for `docs/ja/docs/advanced/index.md`. PR #5043 by @wakabame.
  * 🌐🇵🇱 Add Polish translation for `docs/pl/docs/tutorial/first-steps.md`. PR #5024 by @Valaraucoo.


### Internal¶
  * 🔧 Update translations notification for Hebrew. PR #5158 by @tiangolo.
  * 🔧 Update Dependabot commit message. PR #5156 by @tiangolo.
  * ⬆ Bump actions/upload-artifact from 2 to 3. PR #5148 by @dependabot[bot].
  * ⬆ Bump actions/cache from 2 to 3. PR #5149 by @dependabot[bot].
  * 🔧 Update sponsors badge configs. PR #5155 by @tiangolo.
  * 👥 Update FastAPI People. PR #5154 by @tiangolo.
  * 🔧 Update Jina sponsor badges. PR #5151 by @tiangolo.
  * ⬆ Bump actions/checkout from 2 to 3. PR #5133 by @dependabot[bot].
  * ⬆ [pre-commit.ci] pre-commit autoupdate. PR #5030 by @pre-commit-ci[bot].
  * ⬆ Bump nwtgck/actions-netlify from 1.1.5 to 1.2.3. PR #5132 by @dependabot[bot].
  * ⬆ Bump codecov/codecov-action from 2 to 3. PR #5131 by @dependabot[bot].
  * ⬆ Bump dawidd6/action-download-artifact from 2.9.0 to 2.21.1. PR #5130 by @dependabot[bot].
  * ⬆ Bump actions/setup-python from 2 to 4. PR #5129 by @dependabot[bot].
  * 👷 Add Dependabot. PR #5128 by @tiangolo.
  * ♻️ Move from `Optional[X]` to `Union[X, None]` for internal utils. PR #5124 by @tiangolo.
  * 🔧 Update sponsors, remove Dropbase, add Doist. PR #5096 by @tiangolo.
  * 🔧 Update sponsors, remove Classiq, add ImgWhale. PR #5079 by @tiangolo.


## 0.78.0¶
### Features¶
  * ✨ Add support for omitting `...` as default value when declaring required parameters with:
  * `Path()`
  * `Query()`
  * `Header()`
  * `Cookie()`
  * `Body()`
  * `Form()`
  * `File()`


New docs at Tutorial - Query Parameters and String Validations - Make it required. PR #4906 by @tiangolo.
Up to now, declaring a required parameter while adding additional validation or metadata needed using `...` (Ellipsis).
For example:
```
fromfastapiimport Cookie, FastAPI, Header, Path, Query
app = FastAPI()
@app.get("/items/{item_id}")
defmain(
  item_id: int = Path(default=..., gt=0),
  query: str = Query(default=..., max_length=10),
  session: str = Cookie(default=..., min_length=3),
  x_trace: str = Header(default=..., title="Tracing header"),
):
  return {"message": "Hello World"}

```

...all these parameters are required because the default value is `...` (Ellipsis).
But now it's possible and supported to just omit the default value, as would be done with Pydantic fields, and the parameters would still be required.
✨ For example, this is now supported:
```
fromfastapiimport Cookie, FastAPI, Header, Path, Query
app = FastAPI()
@app.get("/items/{item_id}")
defmain(
  item_id: int = Path(gt=0),
  query: str = Query(max_length=10),
  session: str = Cookie(min_length=3),
  x_trace: str = Header(title="Tracing header"),
):
  return {"message": "Hello World"}

```

To declare parameters as optional (not required), you can set a default value as always, for example using `None`:
```
fromtypingimport Union
fromfastapiimport Cookie, FastAPI, Header, Path, Query
app = FastAPI()
@app.get("/items/{item_id}")
defmain(
  item_id: int = Path(gt=0),
  query: Union[str, None] = Query(default=None, max_length=10),
  session: Union[str, None] = Cookie(default=None, min_length=3),
  x_trace: Union[str, None] = Header(default=None, title="Tracing header"),
):
  return {"message": "Hello World"}

```

### Docs¶
  * 📝 Add docs recommending `Union` over `Optional` and migrate source examples. New docs at Python Types Intro - Using `Union` or `Optional`. PR #4908 by @tiangolo.
  * 🎨 Fix default value as set in tutorial for Path Operations Advanced Configurations. PR #4899 by @tiangolo.
  * 📝 Add documentation for redefined path operations. PR #4864 by @madkinsz.
  * 📝 Updates links for Celery documentation. PR #4736 by @sammyzord.
  * ✏ Fix example code with sets in tutorial for body nested models. PR #3030 by @hitrust.
  * ✏ Fix links to Pydantic docs. PR #4670 by @kinuax.
  * 📝 Update docs about Swagger UI self-hosting with newer source links. PR #4813 by @Kastakin.
  * 📝 Add link to external article: Building the Poll App From Django Tutorial With FastAPI And React. PR #4778 by @jbrocher.
  * 📝 Add OpenAPI warning to "Body - Fields" docs with extra schema extensions. PR #4846 by @ml-evs.


### Translations¶
  * 🌐 Fix code examples in Japanese translation for `docs/ja/docs/tutorial/testing.md`. PR #4623 by @hirotoKirimaru.


### Internal¶
  * ♻ Refactor dict value extraction to minimize key lookups `fastapi/utils.py`. PR #3139 by @ShahriyarR.
  * ✅ Add tests for required nonable parameters and body fields. PR #4907 by @tiangolo.
  * 👷 Fix installing Material for MkDocs Insiders in CI. PR #4897 by @tiangolo.
  * 👷 Add pre-commit CI instead of custom GitHub Action. PR #4896 by @tiangolo.
  * 👷 Add pre-commit GitHub Action workflow. PR #4895 by @tiangolo.
  * 📝 Add dark mode auto switch to docs based on OS preference. PR #4869 by @ComicShrimp.
  * 🔥 Remove un-used old pending tests, already covered in other places. PR #4891 by @tiangolo.
  * 🔧 Add Python formatting hooks to pre-commit. PR #4890 by @tiangolo.
  * 🔧 Add pre-commit with first config and first formatting pass. PR #4888 by @tiangolo.
  * 👷 Disable CI installing Material for MkDocs in forks. PR #4410 by @dolfinus.


## 0.77.1¶
### Upgrades¶
  * ⬆ Upgrade Starlette from 0.19.0 to 0.19.1. PR #4819 by @Kludex.


### Docs¶
  * 📝 Add link to german article: REST-API Programmieren mittels Python und dem FastAPI Modul. PR #4624 by @fschuermeyer.
  * 📝 Add external link: PyCharm Guide to FastAPI. PR #4512 by @mukulmantosh.
  * 📝 Add external link to article: Building an API with FastAPI and Supabase and Deploying on Deta. PR #4440 by @aUnicornDev.
  * ✏ Fix small typo in `docs/en/docs/tutorial/security/first-steps.md`. PR #4515 by @KikoIlievski.


### Translations¶
  * 🌐 Add Polish translation for `docs/pl/docs/tutorial/index.md`. PR #4516 by @MKaczkow.
  * ✏ Fix typo in deployment. PR #4629 by @raisulislam541.
  * 🌐 Add Portuguese translation for `docs/pt/docs/help-fastapi.md`. PR #4583 by @mateusjs.


### Internal¶
  * 🔧 Add notifications in issue for Uzbek translations. PR #4884 by @tiangolo.


## 0.77.0¶
### Upgrades¶
  * ⬆ Upgrade Starlette from 0.18.0 to 0.19.0. PR #4488 by @Kludex.
    * When creating an explicit `JSONResponse` the `content` argument is now required.


### Docs¶
  * 📝 Add external link to article: Seamless FastAPI Configuration with ConfZ. PR #4414 by @silvanmelchior.
  * 📝 Add external link to article: 5 Advanced Features of FastAPI You Should Try. PR #4436 by @kaustubhgupta.
  * ✏ Reword to improve legibility of docs about `TestClient`. PR #4389 by @rgilton.
  * 📝 Add external link to blog post about Kafka, FastAPI, and Ably. PR #4044 by @Ugbot.
  * ✏ Fix typo in `docs/en/docs/tutorial/sql-databases.md`. PR #4875 by @wpyoga.
  * ✏ Fix typo in `docs/en/docs/async.md`. PR #4726 by @Prezu.


### Translations¶
  * 🌐 Update source example highlights for `docs/zh/docs/tutorial/query-params-str-validations.md`. PR #4237 by @caimaoy.
  * 🌐 Remove translation docs references to aiofiles as it's no longer needed since AnyIO. PR #3594 by @alonme.
  * ✏ 🌐 Fix typo in Portuguese translation for `docs/pt/docs/tutorial/path-params.md`. PR #4722 by @CleoMenezesJr.
  * 🌐 Fix live docs server for translations for some languages. PR #4729 by @wakabame.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/cookie-params.md`. PR #4112 by @lbmendes.
  * 🌐 Fix French translation for `docs/tutorial/body.md`. PR #4332 by @Smlep.
  * 🌐 Add Japanese translation for `docs/ja/docs/advanced/conditional-openapi.md`. PR #2631 by @sh0nk.
  * 🌐 Fix Japanese translation of `docs/ja/docs/tutorial/body.md`. PR #3062 by @a-takahashi223.
  * 🌐 Add Portuguese translation for `docs/pt/docs/tutorial/background-tasks.md`. PR #2170 by @izaguerreiro.
  * 🌐 Add Portuguese translation for `docs/deployment/deta.md`. PR #4442 by @lsglucas.
  * 🌐 Add Russian translation for `docs/async.md`. PR #4036 by @Winand.
  * 🌐 Add Portuguese translation for `docs/tutorial/body.md`. PR #3960 by @leandrodesouzadev.
  * 🌐 Add Portuguese translation of `tutorial/extra-data-types.md`. PR #4077 by @luccasmmg.
  * 🌐 Update German translation for `docs/features.md`. PR #3905 by @jomue.


## 0.76.0¶
### Upgrades¶
  * ⬆ Upgrade Starlette from 0.17.1 to 0.18.0. PR #4483 by @Kludex.


### Internal¶
  * 👥 Update FastAPI People. PR #4847 by @github-actions[bot].
  * 🔧 Add Budget Insight sponsor. PR #4824 by @tiangolo.
  * 🍱 Update sponsor, ExoFlare badge. PR #4822 by @tiangolo.
  * 🔧 Update sponsors, enable Dropbase again, update TalkPython link. PR #4821 by @tiangolo.


## 0.75.2¶
This release includes upgrades to third-party packages that handle security issues. Although there's a chance these issues don't affect you in particular, please upgrade as soon as possible.
### Fixes¶
  * ✅ Fix new/recent tests with new fixed `ValidationError` JSON Schema. PR #4806 by @tiangolo.
  * 🐛 Fix JSON Schema for `ValidationError` at field `loc`. PR #3810 by @dconathan.
  * 🐛 Fix support for prefix on APIRouter WebSockets. PR #2640 by @Kludex.


### Upgrades¶
  * ⬆️ Update ujson ranges for CVE-2021-45958. PR #4804 by @tiangolo.
  * ⬆️ Upgrade dependencies upper range for extras "all". PR #4803 by @tiangolo.
  * ⬆ Upgrade Swagger UI - swagger-ui-dist@4. This handles a security issue in Swagger UI itself where it could be possible to inject HTML into Swagger UI. Please upgrade as soon as you can, in particular if you expose your Swagger UI (`/docs`) publicly to non-expert users. PR #4347 by @RAlanWright.


### Internal¶
  * 🔧 Update sponsors, add: ExoFlare, Ines Course; remove: Dropbase, Vim.so, Calmcode; update: Striveworks, TalkPython and TestDriven.io. PR #4805 by @tiangolo.
  * ⬆️ Upgrade Codecov GitHub Action. PR #4801 by @tiangolo.


## 0.75.1¶
### Translations¶
  * 🌐 Start Dutch translations. PR #4703 by @tiangolo.
  * 🌐 Start Persian/Farsi translations. PR #4243 by @aminalaee.
  * ✏ Reword sentence about handling errors. PR #1993 by @khuhroproeza.


### Internal¶
  * 👥 Update FastAPI People. PR #4752 by @github-actions[bot].
  * ➖ Temporarily remove typer-cli from dependencies and upgrade Black to unblock Pydantic CI. PR #4754 by @tiangolo.
  * 🔧 Add configuration to notify Dutch translations. PR #4702 by @tiangolo.
  * 👥 Update FastAPI People. PR #4699 by @github-actions[bot].
  * 🐛 Fix FastAPI People generation to include missing file in commit. PR #4695 by @tiangolo.
  * 🔧 Update Classiq sponsor links. PR #4688 by @tiangolo.
  * 🔧 Add Classiq sponsor. PR #4671 by @tiangolo.
  * 📝 Add Jina's QA Bot to the docs to help people that want to ask quick questions. PR #4655 by @tiangolo based on original PR #4626 by @hanxiao.


## 0.75.0¶
### Features¶
  * ✨ Add support for custom `generate_unique_id_function` and docs for generating clients. New docs: Advanced - Generate Clients. PR #4650 by @tiangolo.


## 0.74.1¶
### Features¶
  * ✨ Include route in scope to allow middleware and other tools to extract its information. PR #4603 by @tiangolo.


## 0.74.0¶
### Breaking Changes¶
  * ✨ Update internal `AsyncExitStack` to fix context for dependencies with `yield`. PR #4575 by @tiangolo.


Dependencies with `yield` can now catch `HTTPException` and custom exceptions. For example:
```
async defget_database():
  with Session() as session:
    try:
      yield session
    except HTTPException:
      session.rollback()
      raise
    finally:
      session.close()

```

After the dependency with `yield` handles the exception (or not) the exception is raised again. So that any exception handlers can catch it, or ultimately the default internal `ServerErrorMiddleware`.
If you depended on exceptions not being received by dependencies with `yield`, and receiving an exception breaks the code after `yield`, you can use a block with `try` and `finally`:
```
async defdo_something():
  try:
    yield something
  finally:
    some_cleanup()

```

...that way the `finally` block is run regardless of any exception that might happen.
### Features¶
  * The same PR #4575 from above also fixes the `contextvars` context for the code before and after `yield`. This was the main objective of that PR.


This means that now, if you set a value in a context variable before `yield`, the value would still be available after `yield` (as you would intuitively expect). And it also means that you can reset the context variable with a token afterwards.
For example, this works correctly now:
```
fromcontextvarsimport ContextVar
fromtypingimport Any, Dict, Optional
legacy_request_state_context_var: ContextVar[Optional[Dict[str, Any]]] = ContextVar(
  "legacy_request_state_context_var", default=None
)
async defset_up_request_state_dependency():
  request_state = {"user": "deadpond"}
  contextvar_token = legacy_request_state_context_var.set(request_state)
  yield request_state
  legacy_request_state_context_var.reset(contextvar_token)

```

...before this change it would raise an error when resetting the context variable, because the `contextvars` context was different, because of the way it was implemented.
**Note** : You probably don't need `contextvars`, and you should probably avoid using them. But they are powerful and useful in some advanced scenarios, for example, migrating from code that used Flask's `g` semi-global variable.
**Technical Details** : If you want to know more of the technical details you can check out the PR description #4575.
### Internal¶
  * 🔧 Add Striveworks sponsor. PR #4596 by @tiangolo.
  * 💚 Only build docs on push when on master to avoid duplicate runs from PRs. PR #4564 by @tiangolo.
  * 👥 Update FastAPI People. PR #4502 by @github-actions[bot].


## 0.73.0¶
### Features¶
  * ✨ Add support for declaring `UploadFile` parameters without explicit `File()`. PR #4469 by @tiangolo. New docs: Request Files - File Parameters with UploadFile.
  * ✨ Add support for tags with Enums. PR #4468 by @tiangolo. New docs: Path Operation Configuration - Tags with Enums.
  * ✨ Allow hiding from OpenAPI (and Swagger UI) `Query`, `Cookie`, `Header`, and `Path` parameters. PR #3144 by @astraldawn. New docs: Query Parameters and String Validations - Exclude from OpenAPI.


### Docs¶
  * 📝 Tweak and improve docs for Request Files. PR #4470 by @tiangolo.


### Fixes¶
  * 🐛 Fix bug preventing to use OpenAPI when using tuples. PR #3874 by @victorbenichoux.
  * 🐛 Prefer custom encoder over defaults if specified in `jsonable_encoder`. PR #2061 by @viveksunder.
    * 💚 Duplicate PR to trigger CI. PR #4467 by @tiangolo.


### Internal¶
  * 🐛 Fix docs dependencies cache, to get the latest Material for MkDocs. PR #4466 by @tiangolo.
  * 🔧 Add sponsor Dropbase. PR #4465 by @tiangolo.


## 0.72.0¶
### Features¶
  * ✨ Enable configuring Swagger UI parameters. Original PR #2568 by @jmriebold. Here are the new docs: Configuring Swagger UI.


### Docs¶
  * 📝 Update Python Types docs, add missing 3.6 / 3.9 example. PR #4434 by @tiangolo.


### Translations¶
  * 🌐 Update Chinese translation for `docs/help-fastapi.md`. PR #3847 by @jaystone776.
  * 🌐 Fix Korean translation for `docs/ko/docs/index.md`. PR #4195 by @kty4119.
  * 🌐 Add Polish translation for `docs/pl/docs/index.md`. PR #4245 by @MicroPanda123.
  * 🌐 Add Chinese translation for `docs\tutorial\path-operation-configuration.md`. PR #3312 by @jaystone776.


### Internal¶
  * 🔧 Enable MkDocs Material Insiders' `content.tabs.link`. PR #4399 by @tiangolo.


## 0.71.0¶
### Features¶
  * ✨ Add docs and tests for Python 3.9 and Python 3.10. PR #3712 by @tiangolo.
    * You can start with Python Types Intro, it explains what changes between different Python versions, in Python 3.9 and in Python 3.10.
    * All the FastAPI docs are updated. Each code example in the docs that could use different syntax in Python 3.9 or Python 3.10 now has all the alternatives in tabs.
  * ⬆️ Upgrade Starlette to 0.17.1. PR #4145 by @simondale00.


### Internal¶
  * 👥 Update FastAPI People. PR #4354 by @github-actions[bot].
  * 🔧 Add FastAPI Trove Classifier for PyPI as now there's one 🤷😁. PR #4386 by @tiangolo.
  * ⬆ Upgrade MkDocs Material and configs. PR #4385 by @tiangolo.


## 0.70.1¶
There's nothing interesting in this particular FastAPI release. It is mainly to enable/unblock the release of the next version of Pydantic that comes packed with features and improvements. 🤩
### Fixes¶
  * 🐛 Fix JSON Schema for dataclasses, supporting the fixes in Pydantic 1.9. PR #4272 by @PrettyWood.


### Translations¶
  * 🌐 Add Korean translation for `docs/tutorial/request-forms-and-files.md`. PR #3744 by @NinaHwang.
  * 🌐 Add Korean translation for `docs/tutorial/request-files.md`. PR #3743 by @NinaHwang.
  * 🌐 Add portuguese translation for `docs/tutorial/query-params-str-validations.md`. PR #3965 by @leandrodesouzadev.
  * 🌐 Add Korean translation for `docs/tutorial/response-status-code.md`. PR #3742 by @NinaHwang.
  * 🌐 Add Korean translation for Tutorial - JSON Compatible Encoder. PR #3152 by @NEONKID.
  * 🌐 Add Korean translation for Tutorial - Path Parameters and Numeric Validations. PR #2432 by @hard-coders.
  * 🌐 Add Korean translation for `docs/ko/docs/deployment/versions.md`. PR #4121 by @DevDae.
  * 🌐 Fix Korean translation for `docs/ko/docs/tutorial/index.md`. PR #4193 by @kimjaeyoonn.
  * 🔧 Add CryptAPI sponsor. PR #4264 by @tiangolo.
  * 📝 Update `docs/tutorial/dependencies/classes-as-dependencies`: Add type of query parameters in a description of `Classes as dependencies`. PR #4015 by @0417taehyun.
  * 🌐 Add French translation for Tutorial - First steps. PR #3455 by @Smlep.
  * 🌐 Add French translation for `docs/tutorial/path-params.md`. PR #3548 by @Smlep.
  * 🌐 Add French translation for `docs/tutorial/query-params.md`. PR #3556 by @Smlep.
  * 🌐 Add Turkish translation for `docs/python-types.md`. PR #3926 by @BilalAlpaslan.


### Internal¶
  * 👥 Update FastAPI People. PR #4274 by @github-actions[bot].


## 0.70.0¶
This release just upgrades Starlette to the latest version, `0.16.0`, which includes several bug fixes and some small breaking changes.
These last **three consecutive releases** are independent so that you can **migrate gradually** :
  * First to FastAPI `0.68.2`, with no breaking changes, but upgrading all the sub-dependencies.
  * Next to FastAPI `0.69.0`, which upgrades Starlette to `0.15.0`, with AnyIO support, and a higher chance of having breaking changes in your code.
  * Finally to FastAPI `0.70.0`, just upgrading Starlette to the latest version `0.16.0` with additional bug fixes.


This way, in case there was a breaking change for your code in one of the releases, you can still benefit from the previous upgrades. ✨
### Breaking Changes - Upgrade¶
  * ⬆️ Upgrade Starlette to 0.16.0. PR #4016 by @tiangolo.


Also upgrades the ranges of optional dependencies:
  * `"jinja2 >=2.11.2,<4.0.0"`
  * `"itsdangerous >=1.1.0,<3.0.0"`


## 0.69.0¶
### Breaking Changes - Upgrade¶
This release adds support for Trio. ✨
It upgrades the version of Starlette to `0.15.0`, now based on AnyIO, and the internal async components in **FastAPI** are now based on AnyIO as well, making it compatible with both **asyncio** and **Trio**.
You can read the docs about running FastAPI with Trio using Hypercorn.
This release also removes `graphene` as an optional dependency for GraphQL. If you need to work with GraphQL, the recommended library now is Strawberry. You can read the new FastAPI with GraphQL docs.
### Features¶
  * ✨ Add support for Trio via AnyIO, upgrading Starlette to `0.15.0`. PR #3372 by @graingert.
  * ➖ Remove `graphene` as an optional dependency. PR #4007 by @tiangolo.


### Docs¶
  * 📝 Add docs for using Trio with Hypercorn. PR #4014 by @tiangolo.
  * ✏ Fix typos in Deployment Guide. PR #3975 by @ghandic.
  * 📝 Update docs with pip install calls when using extras with brackets, use quotes for compatibility with Zsh. PR #3131 by @tomwei7.
  * 📝 Add external link to article: Deploying ML Models as API Using FastAPI and Heroku. PR #3904 by @kaustubhgupta.
  * ✏ Fix typo in file paths in `docs/en/docs/contributing.md`. PR #3752 by @NinaHwang.
  * ✏ Fix a typo in `docs/en/docs/advanced/path-operation-advanced-configuration.md` and `docs/en/docs/release-notes.md`. PR #3750 by @saintmalik.
  * ✏️ Add a missing comma in the security tutorial. PR #3564 by @jalvaradosegura.
  * ✏ Fix typo in `docs/en/docs/help-fastapi.md`. PR #3760 by @jaystone776.
  * ✏ Fix typo about file path in `docs/en/docs/tutorial/bigger-applications.md`. PR #3285 by @HolyDorus.
  * ✏ Re-word to clarify test client in `docs/en/docs/tutorial/testing.md`. PR #3382 by @Bharat123rox.
  * 📝 Fix incorrect highlighted code. PR #3325 by @paxcodes.
  * 📝 Add external link to article: How-to deploy FastAPI app to Heroku. PR #3241 by @Jarmos-san.
  * ✏ Fix typo (mistranslation) in `docs/en/docs/advanced/templates.md`. PR #3211 by @oerpli.
  * 📝 Remove note about (now supported) feature from Swagger UI in `docs/en/docs/tutorial/request-files.md`. PR #2803 by @gsganden.
  * ✏ Fix typo re-word in `docs/tutorial/handling-errors.md`. PR #2700 by @graue70.


### Translations¶
  * 🌐 Initialize Azerbaijani translations. PR #3941 by @madatbay.
  * 🌐 Add Turkish translation for `docs/fastapi-people.md`. PR #3848 by @BilalAlpaslan.


### Internal¶
  * 📝 Add supported Python versions badge. PR #2794 by @hramezani.
  * ✏ Fix link in Japanese docs for `docs/ja/docs/deployment/docker.md`. PR #3245 by @utamori.
  * 🔧 Correct DeprecationWarning config and comment in pytest settings. PR #4008 by @graingert.
  * 🔧 Swap light/dark theme button icon. PR #3246 by @eddsalkield.
  * 🔧 Lint only in Python 3.7 and above. PR #4006 by @tiangolo.
  * 🔧 Add GitHub Action notify-translations config for Azerbaijani. PR #3995 by @tiangolo.


## 0.68.2¶
This release has **no breaking changes**. 🎉
It upgrades the version ranges of sub-dependencies to allow applications using FastAPI to easily upgrade them.
Soon there will be a new FastAPI release upgrading Starlette to take advantage of recent improvements, but as that has a higher chance of having breaking changes, it will be in a separate release.
### Features¶
  * ⬆Increase supported version of aiofiles to suppress warnings. PR #2899 by @SnkSynthesis.
  * ➖ Do not require backports in Python >= 3.7. PR #1880 by @FFY00.
  * ⬆ Upgrade required Python version to >= 3.6.1, needed by typing.Deque, used by Pydantic. PR #2733 by @hukkin.
  * ⬆️ Bump Uvicorn max range to 0.15.0. PR #3345 by @Kludex.


### Docs¶
  * 📝 Update GraphQL docs, recommend Strawberry. PR #3981 by @tiangolo.
  * 📝 Re-write and extend Deployment guide: Concepts, Uvicorn, Gunicorn, Docker, Containers, Kubernetes. PR #3974 by @tiangolo.
  * 📝 Upgrade HTTPS guide with more explanations and diagrams. PR #3950 by @tiangolo.


### Translations¶
  * 🌐 Add Turkish translation for `docs/features.md`. PR #1950 by @ycd.
  * 🌐 Add Turkish translation for `docs/benchmarks.md`. PR #2729 by @Telomeraz.
  * 🌐 Add Turkish translation for `docs/index.md`. PR #1908 by @ycd.
  * 🌐 Add French translation for `docs/tutorial/body.md`. PR #3671 by @Smlep.
  * 🌐 Add French translation for `deployment/docker.md`. PR #3694 by @rjNemo.
  * 🌐 Add Portuguese translation for `docs/tutorial/path-params.md`. PR #3664 by @FelipeSilva93.
  * 🌐 Add Portuguese translation for `docs/deployment/https.md`. PR #3754 by @lsglucas.
  * 🌐 Add German translation for `docs/features.md`. PR #3699 by @mawassk.


### Internal¶
  * ✨ Update GitHub Action: notify-translations, to avoid a race conditions. PR #3989 by @tiangolo.
  * ⬆️ Upgrade development `autoflake`, supporting multi-line imports. PR #3988 by @tiangolo.
  * ⬆️ Increase dependency ranges for tests and docs: pytest-cov, pytest-asyncio, black, httpx, sqlalchemy, databases, mkdocs-markdownextradata-plugin. PR #3987 by @tiangolo.
  * 👥 Update FastAPI People. PR #3986 by @github-actions[bot].
  * 💚 Fix badges in README and main page. PR #3979 by @ghandic.
  * ⬆ Upgrade internal testing dependencies: mypy to version 0.910, add newly needed type packages. PR #3350 by @ArcLightSlavik.
  * ✨ Add Deepset Sponsorship. PR #3976 by @tiangolo.
  * 🎨 Tweak CSS styles for shell animations. PR #3888 by @tiangolo.
  * 🔧 Add new Sponsor Calmcode.io. PR #3777 by @tiangolo.


## 0.68.1¶
  * ✨ Add support for `read_with_orm_mode`, to support SQLModel relationship attributes. PR #3757 by @tiangolo.


### Translations¶
  * 🌐 Add Portuguese translation of `docs/fastapi-people.md`. PR #3461 by @ComicShrimp.
  * 🌐 Add Chinese translation for `docs/tutorial/dependencies/dependencies-in-path-operation-decorators.md`. PR #3492 by @jaystone776.
  * 🔧 Add new Translation tracking issues for German and Indonesian. PR #3718 by @tiangolo.
  * 🌐 Add Chinese translation for `docs/tutorial/dependencies/sub-dependencies.md`. PR #3491 by @jaystone776.
  * 🌐 Add Portuguese translation for `docs/advanced/index.md`. PR #3460 by @ComicShrimp.
  * 🌐 Portuguese translation of `docs/async.md`. PR #1330 by @Serrones.
  * 🌐 Add French translation for `docs/async.md`. PR #3416 by @Smlep.


### Internal¶
  * ✨ Add GitHub Action: Notify Translations. PR #3715 by @tiangolo.
  * ✨ Update computation of FastAPI People and sponsors. PR #3714 by @tiangolo.
  * ✨ Enable recent Material for MkDocs Insiders features. PR #3710 by @tiangolo.
  * 🔥 Remove/clean extra imports from examples in docs for features. PR #3709 by @tiangolo.
  * ➕ Update docs library to include sources in Markdown. PR #3648 by @tiangolo.
  * ⬆ Enable tests for Python 3.9. PR #2298 by @Kludex.
  * 👥 Update FastAPI People. PR #3642 by @github-actions[bot].


## 0.68.0¶
### Features¶
  * ✨ Add support for extensions and updates to the OpenAPI schema in each _path operation_. New docs: FastAPI Path Operation Advanced Configuration - OpenAPI Extra. Initial PR #1922 by @edouardlp.
  * ✨ Add additional OpenAPI metadata parameters to `FastAPI` class, shown on the automatic API docs UI. New docs: Metadata and Docs URLs. Initial PR #1812 by @dkreeft.
  * ✨ Add `description` parameter to all the security scheme classes, e.g. `APIKeyQuery(name="key", description="A very cool API key")`. PR #1757 by @hylkepostma.
  * ✨ Update OpenAPI models, supporting recursive models and extensions. PR #3628 by @tiangolo.
  * ✨ Import and re-export data structures from Starlette, used by Request properties, on `fastapi.datastructures`. Initial PR #1872 by @jamescurtin.


### Docs¶
  * 📝 Update docs about async and response-model with more gender neutral language. PR #1869 by @Edward-Knight.


### Translations¶
  * 🌐 Add Russian translation for `docs/python-types.md`. PR #3039 by @dukkee.
  * 🌐 Add Chinese translation for `docs/tutorial/dependencies/index.md`. PR #3489 by @jaystone776.
  * 🌐 Add Russian translation for `docs/external-links.md`. PR #3036 by @dukkee.
  * 🌐 Add Chinese translation for `docs/tutorial/dependencies/global-dependencies.md`. PR #3493 by @jaystone776.
  * 🌐 Add Portuguese translation for `docs/deployment/versions.md`. PR #3618 by @lsglucas.
  * 🌐 Add Japanese translation for `docs/tutorial/security/oauth2-jwt.md`. PR #3526 by @sattosan.


### Internal¶
  * ✅ Add the `docs_src` directory to test coverage and update tests. Initial PR #1904 by @Kludex.
  * 🔧 Add new GitHub templates with forms for new issues. PR #3612 by @tiangolo.
  * 📝 Add official FastAPI Twitter to docs: @fastapi. PR #3578 by @tiangolo.


## 0.67.0¶
### Features¶
  * ✨ Add support for `dataclasses` in request bodies and `response_model`. New documentation: Advanced User Guide - Using Dataclasses. PR #3577 by @tiangolo.
  * ✨ Support `dataclasses` in responses. PR #3576 by @tiangolo, continuation from initial PR #2722 by @amitlissack.


### Docs¶
  * 📝 Add external link: How to Create A Fake Certificate Authority And Generate TLS Certs for FastAPI. PR #2839 by @aitoehigie.
  * ✏ Fix code highlighted line in: `body-nested-models.md`. PR #3463 by @jaystone776.
  * ✏ Fix typo in `body-nested-models.md`. PR #3462 by @jaystone776.
  * ✏ Fix typo "might me" -> "might be" in `docs/en/docs/tutorial/schema-extra-example.md`. PR #3362 by @dbrakman.
  * 📝 Add external link: Building simple E-Commerce with NuxtJS and FastAPI. PR #3271 by @ShahriyarR.
  * 📝 Add external link: Serve a machine learning model using Sklearn, FastAPI and Docker. PR #2974 by @rodrigo-arenas.
  * ✏️ Fix typo on docstring in datastructures file. PR #2887 by @Kludex.
  * 📝 Add External Link: Deploy FastAPI on Ubuntu and Serve using Caddy 2 Web Server. PR #3572 by @tiangolo.
  * 📝 Add External Link, replaces #1898. PR #3571 by @tiangolo.


### Internal¶
  * 🎨 Improve style for sponsors, add radius border. PR #2388 by @Kludex.
  * 👷 Update GitHub Action latest-changes. PR #3574 by @tiangolo.
  * 👷 Update GitHub Action latest-changes. PR #3573 by @tiangolo.
  * 👷 Rename and clarify CI workflow job names. PR #3570 by @tiangolo.
  * 👷 Update GitHub Action latest-changes, strike 2 ⚾. PR #3575 by @tiangolo.
  * 🔧 Sort external links in docs to have the most recent at the top. PR #3568 by @tiangolo.


## 0.66.1¶
### Translations¶
  * 🌐 Add basic setup for German translations. PR #3522 by @0x4Dark.
  * 🌐 Add Portuguese translation for `docs/tutorial/security/index.md`. PR #3507 by @oandersonmagalhaes.
  * 🌐 Add Portuguese translation for `docs/deployment/index.md`. PR #3337 by @lsglucas.


### Internal¶
  * 🔧 Configure strict pytest options and update/refactor tests. Upgrade pytest to `>=6.2.4,<7.0.0` and pytest-cov to `>=2.12.0,<3.0.0`. Initial PR #2790 by @graingert.
  * ⬆️ Upgrade python-jose dependency to `>=3.3.0,<4.0.0` for tests. PR #3468 by @tiangolo.


## 0.66.0¶
### Features¶
  * ✨ Allow setting the `response_class` to `RedirectResponse` or `FileResponse` and returning the URL from the function. New and updated docs are in the tutorial section **Custom Response - HTML, Stream, File, others** , in RedirectResponse and in FileResponse. PR #3457 by @tiangolo.


### Fixes¶
  * 🐛 Fix include/exclude for dicts in `jsonable_encoder`. PR #2016 by @Rubikoid.
  * 🐛 Support custom OpenAPI / JSON Schema fields in the generated output OpenAPI. PR #1429 by @jmagnusson.


### Translations¶
  * 🌐 Add Spanish translation for `tutorial/query-params.md`. PR #2243 by @mariacamilagl.
  * 🌐 Add Spanish translation for `advanced/response-directly.md`. PR #1253 by @jfunez.
  * 🌐 Add Spanish translation for `advanced/additional-status-codes.md`. PR #1252 by @jfunez.
  * 🌐 Add Spanish translation for `advanced/path-operation-advanced-configuration.md`. PR #1251 by @jfunez.


## 0.65.3¶
### Fixes¶
  * ♻ Assume request bodies contain JSON when no Content-Type header is provided. This fixes a breaking change introduced by 0.65.2 with PR #2118. It should allow upgrading FastAPI applications with clients that send JSON data without a `Content-Type` header. And there's still protection against CSRFs. PR #3456 by @tiangolo.


### Translations¶
  * 🌐 Initialize Indonesian translations. PR #3014 by @pace-noge.
  * 🌐 Add Spanish translation of Tutorial - Path Parameters. PR #2219 by @mariacamilagl.
  * 🌐 Add Spanish translation of Tutorial - First Steps. PR #2208 by @mariacamilagl.
  * 🌐 Portuguese translation of Tutorial - Body - Fields. PR #3420 by @ComicShrimp.
  * 🌐 Add Chinese translation for Tutorial - Request - Forms - and - Files. PR #3249 by @jaystone776.
  * 🌐 Add Chinese translation for Tutorial - Handling - Errors. PR #3299 by @jaystone776.
  * 🌐 Add Chinese translation for Tutorial - Form - Data. PR #3248 by @jaystone776.
  * 🌐 Add Chinese translation for Tutorial - Body - Updates. PR #3237 by @jaystone776.
  * 🌐 Add Chinese translation for FastAPI People. PR #3112 by @hareru.
  * 🌐 Add French translation for Project Generation. PR #3197 by @Smlep.
  * 🌐 Add French translation for Python Types Intro. PR #3185 by @Smlep.
  * 🌐 Add French translation for External Links. PR #3103 by @Smlep.
  * 🌐 Add French translation for Alternatives, Inspiration and Comparisons. PR #3020 by @rjNemo.
  * 🌐 Fix Chinese translation code snippet mismatch in Tutorial - Python Types Intro. PR #2573 by @BoYanZh.
  * 🌐 Add Portuguese translation for Development Contributing. PR #1364 by @Serrones.
  * 🌐 Add Chinese translation for Tutorial - Request - Files. PR #3244 by @jaystone776.


### Internal¶
  * 👥 Update FastAPI People. PR #3450 by @github-actions[bot].
  * 👥 Update FastAPI People. PR #3319 by @github-actions[bot].
  * ⬆ Upgrade docs development dependency on `typer-cli` to >=0.0.12 to fix conflicts. PR #3429 by @tiangolo.


## 0.65.2¶
### Security fixes¶
  * 🔒 Check Content-Type request header before assuming JSON. Initial PR #2118 by @patrickkwang.


This change fixes a CSRF security vulnerability when using cookies for authentication in path operations with JSON payloads sent by browsers.
In versions lower than `0.65.2`, FastAPI would try to read the request payload as JSON even if the `content-type` header sent was not set to `application/json` or a compatible JSON media type (e.g. `application/geo+json`).
So, a request with a content type of `text/plain` containing JSON data would be accepted and the JSON data would be extracted.
But requests with content type `text/plain` are exempt from CORS preflights, for being considered Simple requests. So, the browser would execute them right away including cookies, and the text content could be a JSON string that would be parsed and accepted by the FastAPI application.
See CVE-2021-32677 for more details.
Thanks to Dima Boger for the security report! 🙇🔒
### Internal¶
  * 🔧 Update sponsors badge, course bundle. PR #3340 by @tiangolo.
  * 🔧 Add new gold sponsor Jina 🎉. PR #3291 by @tiangolo.
  * 🔧 Add new banner sponsor badge for FastAPI courses bundle. PR #3288 by @tiangolo.
  * 👷 Upgrade Issue Manager GitHub Action. PR #3236 by @tiangolo.


## 0.65.1¶
### Security fixes¶
  * 📌 Upgrade pydantic pin, to handle security vulnerability CVE-2021-29510. PR #3213 by @tiangolo.


## 0.65.0¶
### Breaking Changes - Upgrade¶
  * ⬆️ Upgrade Starlette to `0.14.2`, including internal `UJSONResponse` migrated from Starlette. This includes several bug fixes and features from Starlette. PR #2335 by @hanneskuettner.


### Translations¶
  * 🌐 Initialize new language Polish for translations. PR #3170 by @neternefer.


### Internal¶
  * 👷 Add GitHub Action cache to speed up CI installs. PR #3204 by @tiangolo.
  * ⬆️ Upgrade setup-python GitHub Action to v2. PR #3203 by @tiangolo.
  * 🐛 Fix docs script to generate a new translation language with `overrides` boilerplate. PR #3202 by @tiangolo.
  * ✨ Add new Deta banner badge with new sponsorship tier 🙇. PR #3194 by @tiangolo.
  * 👥 Update FastAPI People. PR #3189 by @github-actions[bot].
  * 🔊 Update FastAPI People to allow better debugging. PR #3188 by @tiangolo.


## 0.64.0¶
### Features¶
  * ✨ Add support for adding multiple `examples` in request bodies and path, query, cookie, and header params. New docs: Declare Request Example Data. Initial PR #1267 by @austinorr.


### Fixes¶
  * 📌 Pin SQLAlchemy range for tests, as it doesn't use SemVer. PR #3001 by @tiangolo.
  * 🎨 Add newly required type annotations for mypy. PR #2882 by @tiangolo.
  * 🎨 Remove internal "type: ignore", now unnecessary. PR #2424 by @AsakuraMizu.


### Docs¶
  * 📝 Add link to article in Russian "FastAPI: знакомимся с фреймворком". PR #2564 by @trkohler.
  * 📝 Add external link to blog post "Authenticate Your FastAPI App with Auth0". PR #2172 by @dompatmore.
  * 📝 Fix broken link to article: Machine learning model serving in Python using FastAPI and Streamlit. PR #2557 by @davidefiocco.
  * 📝 Add FastAPI Medium Article: Deploy a dockerized FastAPI application to AWS. PR #2515 by @vjanz.
  * ✏ Fix typo in Tutorial - Handling Errors. PR #2486 by @johnthagen.
  * ✏ Fix typo in Security OAuth2 scopes. PR #2407 by @jugmac00.
  * ✏ Fix typo/clarify docs for SQL (Relational) Databases. PR #2393 by @kangni.
  * 📝 Add external link to "FastAPI for Flask Users". PR #2280 by @amitness.


### Translations¶
  * 🌐 Fix Chinese translation of Tutorial - Query Parameters, remove obsolete content. PR #3051 by @louis70109.
  * 🌐 Add French translation for Tutorial - Background Tasks. PR #3098 by @Smlep.
  * 🌐 Fix Korean translation for docs/ko/docs/index.md. PR #3159 by @SueNaEunYang.
  * 🌐 Add Korean translation for Tutorial - Query Parameters. PR #2390 by @hard-coders.
  * 🌐 Add French translation for FastAPI People. PR #2232 by @JulianMaurin.
  * 🌐 Add Korean translation for Tutorial - Path Parameters. PR #2355 by @hard-coders.
  * 🌐 Add French translation for Features. PR #2157 by @Jefidev.
  * 👥 Update FastAPI People. PR #3031 by @github-actions[bot].
  * 🌐 Add Chinese translation for Tutorial - Debugging. PR #2737 by @blt232018.
  * 🌐 Add Chinese translation for Tutorial - Security - OAuth2 with Password (and hashing), Bearer with JWT tokens. PR #2642 by @waynerv.
  * 🌐 Add Korean translation for Tutorial - Header Parameters. PR #2589 by @mode9.
  * 🌐 Add Chinese translation for Tutorial - Metadata and Docs URLs. PR #2559 by @blt232018.
  * 🌐 Add Korean translation for Tutorial - First Steps. PR #2323 by @hard-coders.
  * 🌐 Add Chinese translation for Tutorial - CORS (Cross-Origin Resource Sharing). PR #2540 by @blt232018.
  * 🌐 Add Chinese translation for Tutorial - Middleware. PR #2334 by @lpdswing.
  * 🌐 Add Korean translation for Tutorial - Intro. PR #2317 by @hard-coders.
  * 🌐 Add Chinese translation for Tutorial - Bigger Applications - Multiple Files. PR #2453 by @waynerv.
  * 🌐 Add Chinese translation for Tutorial - Security - Security Intro. PR #2443 by @waynerv.
  * 🌐 Add Chinese translation for Tutorial - Header Parameters. PR #2412 by @maoyibo.
  * 🌐 Add Chinese translation for Tutorial - Extra Data Types. PR #2410 by @maoyibo.
  * 🌐 Add Japanese translation for Deployment - Docker. PR #2312 by @tokusumi.
  * 🌐 Add Japanese translation for Deployment - Versions. PR #2310 by @tokusumi.
  * 🌐 Add Chinese translation for Tutorial - Cookie Parameters. PR #2261 by @alicrazy1947.
  * 🌐 Add Japanese translation for Tutorial - Static files. PR #2260 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Testing. PR #2259 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Debugging. PR #2256 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Middleware. PR #2255 by @tokusumi.
  * 🌐 Add Japanese translation for Concurrency and async / await. PR #2058 by @tokusumi.
  * 🌐 Add Chinese translation for Tutorial - Security - Simple OAuth2 with Password and Bearer. PR #2514 by @waynerv.
  * 🌐 Add Japanese translation for Deployment - Deta. PR #2314 by @tokusumi.
  * 🌐 Add Chinese translation for Tutorial - Security - Get Current User. PR #2474 by @waynerv.
  * 🌐 Add Japanese translation for Deployment - Manually. PR #2313 by @tokusumi.
  * 🌐 Add Japanese translation for Deployment - Intro. PR #2309 by @tokusumi.
  * 🌐 Add Japanese translation for FastAPI People. PR #2254 by @tokusumi.
  * 🌐 Add Japanese translation for Advanced - Path Operation Advanced Configuration. PR #2124 by @Attsun1031.
  * 🌐 Add Japanese translation for External Links. PR #2070 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Body - Updates. PR #1956 by @SwftAlpc.
  * 🌐 Add Japanese translation for Tutorial - Form Data. PR #1943 by @SwftAlpc.
  * 🌐 Add Japanese translation for Tutorial - Cookie Parameters. PR #1933 by @SwftAlpc.


### Internal¶
  * 🔧 Update top banner, point to newsletter. PR #3003 by @tiangolo.
  * 🔧 Disable sponsor WeTransfer. PR #3002 by @tiangolo.
  * 👥 Update FastAPI People. PR #2880 by @github-actions[bot].
  * 👥 Update FastAPI People. PR #2739 by @github-actions[bot].
  * 🔧 Add new Gold Sponsor Talk Python 🎉. PR #2673 by @tiangolo.
  * 🔧 Add new Gold Sponsor vim.so 🎉. PR #2669 by @tiangolo.
  * 🔧 Add FastAPI user survey banner. PR #2623 by @tiangolo.
  * 🔧 Add new Bronze Sponsor(s) 🥉🎉. PR #2622 by @tiangolo.
  * 📝 Update social links: add Discord, fix GitHub. PR #2621 by @tiangolo.
  * 🔧 Update FastAPI People GitHub Sponsors order. PR #2620 by @tiangolo.
  * 🔧 Update InvestSuite sponsor data. PR #2608 by @tiangolo.
  * 👥 Update FastAPI People. PR #2590 by @github-actions[bot].


## 0.63.0¶
### Features¶
  * ✨ Improve type annotations, add support for mypy --strict, internally and for external packages. PR #2547 by @tiangolo.


### Breaking changes¶
  * ⬆️ Upgrade Uvicorn when installing `fastapi[all]` to the latest version including `uvloop`, the new range is `uvicorn[standard] >=0.12.0,<0.14.0`. PR #2548 by @tiangolo.


### Fixes¶
  * 🐛 PR #2547 (read above) also fixes some false-positive mypy errors with `callbacks` parameters and when using the `OAuth2` class.


### Docs¶
  * 📝 Update Uvicorn installation instructions to use uvicorn[standard] (includes uvloop). PR #2543 by @tiangolo.
  * 📝 Update title for Deta tutorial. PR #2466 by @tiangolo.
  * 👥 Update FastAPI People. PR #2454 by @github-actions[bot].


### Translations¶
  * 🌐 Add docs lang selector widget. PR #2542 by @tiangolo.
  * 🌐 Add Chinese translation for Tutorial - Response Status Code. PR #2442 by @waynerv.
  * 🌐 Start translation of the documentation for the Albanian language. PR #2516 by @vjanz.
  * 🌐 Add Chinese translation for Tutorial - Extra Models. PR #2416 by @waynerv.
  * 🌐 Add Chinese translation for Tutorial - Response Model. PR #2414 by @waynerv.
  * 🌐 Add Chinese translation for Tutorial - Schema Extra Example. PR #2411 by @maoyibo.
  * 🌐 Add Korean translation for Index. PR #2192 by @hard-coders.
  * 🌐 Add Japanese translation for Advanced User Guide - Additional Status Codes. PR #2145 by @Attsun1031.


### Internal¶
  * 🐛 Fix docs overrides directory for translations. PR #2541 by @tiangolo.
  * ➖ Remove Typer as a docs building dependency (covered by typer-cli) to fix pip resolver conflicts. PR #2539 by @tiangolo.
  * ✨ Add newsletter: FastAPI and friends. PR #2509 by @tiangolo.
  * ✨ Add new Gold Sponsor: InvestSuite 🎉. PR #2508 by @tiangolo.
  * 🔧 Add issue template configs. PR #2476 by @tiangolo.


## 0.62.0¶
### Features¶
  * ✨ Add support for shared/top-level parameters (dependencies, tags, etc). PR #2434 by @tiangolo.


Up to now, for several options, the only way to apply them to a group of _path operations_ was in `include_router`. That works well, but the call to `app.include_router()` or `router.include_router()` is normally done in another file.
That means that, for example, to apply authentication to all the _path operations_ in a router it would end up being done in a different file, instead of keeping related logic together.
Setting options in `include_router` still makes sense in some cases, for example, to override or increase configurations from a third party router included in an app. But in a router that is part of a bigger application, it would probably make more sense to add those settings when creating the `APIRouter`.
**In`FastAPI`**
This allows setting the (mostly new) parameters (additionally to the already existing parameters):
  * `default_response_class`: updated to handle defaults in `APIRouter` and `include_router`.
  * `dependencies`: to include ✨ top-level dependencies ✨ that apply to the whole application. E.g. to add global authentication.
  * `callbacks`: OpenAPI callbacks that apply to all the _path operations_.
  * `deprecated`: to mark all the _path operations_ as deprecated. 🤷
  * `include_in_schema`: to allow excluding all the _path operations_ from the OpenAPI schema.
  * `responses`: OpenAPI responses that apply to all the _path operations_.


For example:
```
fromfastapiimport FastAPI, Depends
async defsome_dependency():
  return
app = FastAPI(dependencies=[Depends(some_dependency)])

```

**In`APIRouter`**
This allows setting the (mostly new) parameters (additionally to the already existing parameters):
  * `default_response_class`: updated to handle defaults in `APIRouter` and `include_router`. For example, it's not needed to set it explicitly when creating callbacks.
  * `dependencies`: to include ✨ router-level dependencies ✨ that apply to all the _path operations_ in a router. Up to now, this was only possible with `include_router`.
  * `callbacks`: OpenAPI callbacks that apply to all the _path operations_ in this router.
  * `deprecated`: to mark all the _path operations_ in a router as deprecated.
  * `include_in_schema`: to allow excluding all the _path operations_ in a router from the OpenAPI schema.
  * `responses`: OpenAPI responses that apply to all the _path operations_ in a router.
  * `prefix`: to set the path prefix for a router. Up to now, this was only possible when calling `include_router`.
  * `tags`: OpenAPI tags to apply to all the _path operations_ in this router.


For example:
```
fromfastapiimport APIRouter, Depends
async defsome_dependency():
  return
router = APIRouter(prefix="/users", dependencies=[Depends(some_dependency)])

```

**In`include_router`**
Most of these settings are now supported in `APIRouter`, which normally lives closer to the related code, so it is recommended to use `APIRouter` when possible.
But `include_router` is still useful to, for example, adding options (like `dependencies`, `prefix`, and `tags`) when including a third party router, or a generic router that is shared between several projects.
This PR allows setting the (mostly new) parameters (additionally to the already existing parameters):
  * `default_response_class`: updated to handle defaults in `APIRouter` and `FastAPI`.
  * `deprecated`: to mark all the _path operations_ in a router as deprecated in OpenAPI.
  * `include_in_schema`: to allow disabling all the _path operations_ from showing in the OpenAPI schema.
  * `callbacks`: OpenAPI callbacks that apply to all the _path operations_ in this router.


Note: all the previous parameters are still there, so it's still possible to declare `dependencies` in `include_router`.
### Breaking Changes¶
  * PR #2434 includes several improvements that shouldn't affect normal use cases, but could affect in advanced scenarios:
    * If you are testing the generated OpenAPI (you shouldn't, FastAPI already tests it extensively for you): the order for `tags` in `include_router` and _path operations_ was updated for consistency, but it's a simple order change.
    * If you have advanced custom logic to access each route's `route.response_class`, or the `router.default_response_class`, or the `app.default_response_class`: the default value for `response_class` in `APIRoute` and for `default_response_class` in `APIRouter` and `FastAPI` is now a `DefaultPlaceholder` used internally to handle and solve default values and overrides. The actual response class inside the `DefaultPlaceholder` is available at `route.response_class.value`.


### Docs¶
  * PR #2434 (above) includes new or updated docs:
    * Advanced User Guide - OpenAPI Callbacks.
    * Tutorial - Bigger Applications.
    * Tutorial - Dependencies - Dependencies in path operation decorators.
    * Tutorial - Dependencies - Global Dependencies.
  * 📝 Add FastAPI monitoring blog post to External Links. PR #2324 by @louisguitton.
  * ✏️ Fix typo in Deta tutorial. PR #2320 by @tiangolo.
  * ✨ Add Discord chat. PR #2322 by @tiangolo.
  * 📝 Fix image links for sponsors. PR #2304 by @tiangolo.


### Translations¶
  * 🌐 Add Japanese translation for Advanced - Custom Response. PR #2193 by @Attsun1031.
  * 🌐 Add Chinese translation for Benchmarks. PR #2119 by @spaceack.
  * 🌐 Add Chinese translation for Tutorial - Body - Nested Models. PR #1609 by @waynerv.
  * 🌐 Add Chinese translation for Advanced - Custom Response. PR #1459 by @RunningIkkyu.
  * 🌐 Add Chinese translation for Advanced - Return a Response Directly. PR #1452 by @RunningIkkyu.
  * 🌐 Add Chinese translation for Advanced - Additional Status Codes. PR #1451 by @RunningIkkyu.
  * 🌐 Add Chinese translation for Advanced - Path Operation Advanced Configuration. PR #1447 by @RunningIkkyu.
  * 🌐 Add Chinese translation for Advanced User Guide - Intro. PR #1445 by @RunningIkkyu.


### Internal¶
  * 🔧 Update TestDriven link to course in sponsors section. PR #2435 by @tiangolo.
  * 🍱 Update sponsor logos. PR #2418 by @tiangolo.
  * 💚 Fix disabling install of Material for MkDocs Insiders in forks, strike 1 ⚾. PR #2340 by @tiangolo.
  * 🐛 Fix disabling Material for MkDocs Insiders install in forks. PR #2339 by @tiangolo.
  * ✨ Add silver sponsor WeTransfer. PR #2338 by @tiangolo.
  * ✨ Set up and enable Material for MkDocs Insiders for the docs. PR #2325 by @tiangolo.


## 0.61.2¶
### Fixes¶
  * 📌 Relax Swagger UI version pin. PR #2089 by @jmriebold.
  * 🐛 Fix bug overriding custom HTTPException and RequestValidationError from exception_handlers. PR #1924 by @uriyyo.
  * ✏️ Fix typo on dependencies utils and cleanup unused variable. PR #1912 by @Kludex.


### Docs¶
  * ✏️ Fix typo in Tutorial - Path Parameters. PR #2231 by @mariacamilagl.
  * ✏ Fix a stylistic error in docs. PR #2206 by @ddobrinskiy.
  * ✏ Fix capitalizaiton typo in docs. PR #2204 by @imba-tjd.
  * ✏ Fix typo in docs. PR #2179 by @ammarasmro.
  * 📝 Update/fix links in docs to use HTTPS. PR #2165 by @imba-tjd.
  * ✏ Fix typos and add rewording in docs. PR #2159 by @nukopy.
  * 📝 Fix code consistency in examples for Tutorial - User Guide - Path Parameters. PR #2158 by @nukopy.
  * 📝 Fix renamed parameter `content_type` typo. PR #2135 by @TeoZosa.
  * ✏ Fix minor typos in docs. PR #2122 by @TeoZosa.
  * ✏ Fix typos in docs and source examples. PR #2102 by @AdrianDeAnda.
  * ✏ Fix incorrect Celery URLs in docs. PR #2100 by @CircleOnCircles.
  * 📝 Simplify intro to Python Types, all currently supported Python versions include type hints 🎉. PR #2085 by @ninjaaron.
  * 📝 Fix example code with sets in Tutorial - Body - Nested Models 3. PR #2054 by @hitrust.
  * 📝 Fix example code with sets in Tutorial - Body - Nested Models 2. PR #2053 by @hitrust.
  * 📝 Fix example code with sets in Tutorial - Body - Nested Models. PR #2052 by @hitrust.
  * ✏ Fix typo in Benchmarks. PR #1995 by @AlejoAsd.
  * 📝 Add note in CORS tutorial about allow_origins with ["*"] and allow_credentials. PR #1895 by @dsmurrell.
  * 📝 Add deployment to Deta, the first gold sponsor 🎉. PR #2303 by @tiangolo.
  * 👥 Update FastAPI People. PR #2282 by @github-actions[bot].
  * ✏️ Fix uppercase in Tutorial - Query parameters. PR #2245 by @mariacamilagl.
  * 📝 Add articles to External Links. PR #2247 by @tiangolo.
  * ✏ Fix typo in Spanish tutorial index. PR #2020 by @aviloncho.


### Translations¶
  * 🌐 Add Japanese translation for Advanced Tutorial - Response Directly. PR #2191 by @Attsun1031.
  * 📝 Add Japanese translation for Tutorial - Security - First Steps. PR #2153 by @komtaki.
  * 🌐 Add Japanese translation for Tutorial - Query Parameters and String Validations. PR #1901 by @SwftAlpc.
  * 🌐 Add Portuguese translation for External Links. PR #1443 by @Serrones.
  * 🌐 Add Japanese translation for Tutorial - CORS. PR #2125 by @tokusumi.
  * 🌐 Add Japanese translation for Contributing. PR #2067 by @komtaki.
  * 🌐 Add Japanese translation for Project Generation. PR #2050 by @tokusumi.
  * 🌐 Add Japanese translation for Alternatives. PR #2043 by @Attsun1031.
  * 🌐 Add Japanese translation for History Design and Future. PR #2002 by @komtaki.
  * 🌐 Add Japanese translation for Benchmarks. PR #1992 by @komtaki.
  * 🌐 Add Japanese translation for Tutorial - Header Parameters. PR #1935 by @SwftAlpc.
  * 🌐 Add Portuguese translation for Tutorial - First Steps. PR #1861 by @jessicapaz.
  * 🌐 Add Portuguese translation for Python Types. PR #1796 by @izaguerreiro.
  * 🌐 Add Japanese translation for Help FastAPI. PR #1692 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Body. PR #1683 by @tokusumi.
  * 🌐 Add Japanese translation for Tutorial - Query Params. PR #1674 by @tokusumi.
  * 🌐 Add Japanese translation for tutorial/path-params.md. PR #1671 by @tokusumi.
  * 🌐 Add Japanese translation for tutorial/first-steps.md. PR #1658 by @tokusumi.
  * 🌐 Add Japanese translation for tutorial/index.md. PR #1656 by @tokusumi.
  * 🌐 Add translation to Portuguese for Project Generation. PR #1602 by @Serrones.
  * 🌐 Add Japanese translation for Features. PR #1625 by @tokusumi.
  * 🌐 Initialize new language Korean for translations. PR #2018 by @hard-coders.
  * 🌐 Add Portuguese translation of Deployment. PR #1374 by @Serrones.


### Internal¶
  * 🔥 Cleanup after upgrade for Docs Previews GitHub Action. PR #2248 by @tiangolo.
  * 🐛 Fix CI docs preview, unzip docs. PR #2246 by @tiangolo.
  * ✨ Add instant docs deploy previews for PRs from forks. PR #2244 by @tiangolo.
  * ⚡️ Build docs for languages in parallel in subprocesses to speed up CI. PR #2242 by @tiangolo.
  * 🐛 Fix docs order generation for partial translations. PR #2238 by @tiangolo.
  * 👥 Update FastAPI People. PR #2202 by @github-actions[bot].
  * ♻️ Update FastAPI People GitHub Action to send the PR as github-actions. PR #2201 by @tiangolo.
  * 🔧 Update FastAPI People GitHub Action config, run monthly. PR #2199 by @tiangolo.
  * 🐛 Fix FastAPI People GitHub Action Docker dependency, strike 1 ⚾. PR #2198 by @tiangolo.
  * 🐛 Fix FastAPI People GitHub Action Docker dependencies. PR #2197 by @tiangolo.
  * 🐛 Fix FastAPI People GitHub Action when there's nothing to change. PR #2196 by @tiangolo.
  * 👥 Add new section FastAPI People. PR #2195 by @tiangolo.
  * ⬆️ Upgrade GitHub Action Latest Changes. PR #2190 by @tiangolo.
  * ⬆️ Upgrade GitHub Action Label Approved. PR #2189 by @tiangolo.
  * 🔧 Update GitHub Action Label Approved, run at 12:00. PR #2185 by @tiangolo.
  * 👷 Upgrade GitHub Action Latest Changes. PR #2184 by @tiangolo.
  * 👷 Set GitHub Action Label Approved to run daily, not every minute. PR #2163 by @tiangolo.
  * 🔥 Remove pr-approvals GitHub Action as it's not compatible with forks. Use the new one. PR #2162 by @tiangolo.
  * 👷 Add GitHub Action Latest Changes. PR #2160.
  * 👷 Add GitHub Action Label Approved. PR #2161.


## 0.61.1¶
### Fixes¶
  * Fix issues using `jsonable_encoder` with SQLAlchemy models directly. PR #1987.


### Docs¶
  * Fix typo in NoSQL docs. PR #1980 by @facundojmaero.


### Translations¶
  * Add translation for main page to Japanese PR #1571 by @ryuckel.
  * Initialize French translations. PR #1975 by @JulianMaurin-BM.
  * Initialize Turkish translations. PR #1905 by @ycd.


### Internal¶
  * Improve docs maintainability by updating `hl_lines` syntax to use ranges. PR #1863 by @la-mar.


## 0.61.0¶
### Features¶
  * Add support for injecting `HTTPConnection` (as `Request` and `WebSocket`). Useful for sharing app state in dependencies. PR #1827 by @nsidnev.
  * Export `WebSocketDisconnect` and add example handling WebSocket disconnections to docs. PR #1822 by @rkbeatss.


### Breaking Changes¶
  * Require Pydantic > `1.0.0`.
    * Remove support for deprecated Pydantic `0.32.2`. This improves maintainability and allows new features.
    * In `FastAPI` and `APIRouter`:
      * Remove _path operation decorators_ related/deprecated parameter `response_model_skip_defaults` (use `response_model_exclude_unset` instead).
      * Change _path operation decorators_ parameter default for `response_model_exclude` from `set()` to `None` (as is in Pydantic).
    * In `encoders.jsonable_encoder`:
      * Remove deprecated `skip_defaults`, use instead `exclude_unset`.
      * Set default of `exclude` from `set()` to `None` (as is in Pydantic).
    * PR #1862.
  * In `encoders.jsonable_encoder` remove parameter `sqlalchemy_safe`.
    * It was an early hack to allow returning SQLAlchemy models, but it was never documented, and the recommended way is using Pydantic's `orm_mode` as described in the tutorial: SQL (Relational) Databases.
    * PR #1864.


### Docs¶
  * Add link to the course by TestDriven.io: Test-Driven Development with FastAPI and Docker. PR #1860.
  * Fix empty log message in docs example about handling errors. PR #1815 by @manlix.
  * Reword text to reduce ambiguity while not being gender-specific. PR #1824 by @Mause.


### Internal¶
  * Add Flake8 linting. Original PR #1774 by @MashhadiNima.
  * Disable Gitter bot, as it's currently broken, and Gitter's response doesn't show the problem. PR #1853.


## 0.60.2¶
  * Fix typo in docs for query parameters. PR #1832 by @ycd.
  * Add docs about Async Tests. PR #1619 by @empicano.
  * Raise an exception when using form data (`Form`, `File`) without having `python-multipart` installed.
    * Up to now the application would run, and raise an exception only when receiving a request with form data, the new behavior, raising early, will prevent from deploying applications with broken dependencies.
    * It also detects if the correct package `python-multipart` is installed instead of the incorrect `multipart` (both importable as `multipart`).
    * PR #1851 based on original PR #1627 by @chrisngyn, @YKo20010, @kx-chen.
  * Re-enable Gitter releases bot. PR #1831.
  * Add link to async SQL databases tutorial from main SQL tutorial. PR #1813 by @short2strings.
  * Fix typo in tutorial about behind a proxy. PR #1807 by @toidi.
  * Fix typo in Portuguese docs. PR #1795 by @izaguerreiro.
  * Add translations setup for Ukrainian. PR #1830.
  * Add external link Build And Host Fast Data Science Applications Using FastAPI. PR #1786 by @Kludex.
  * Fix encoding of Pydantic models that inherit from others models with custom `json_encoders`. PR #1769 by @henrybetts.
  * Simplify and improve `jsonable_encoder`. PR #1754 by @MashhadiNima.
  * Simplify internal code syntax in several points. PR #1753 by @uriyyo.
  * Improve internal typing, declare `Optional` parameters. PR #1731 by @MashhadiNima.
  * Add external link Deploy FastAPI on Azure App Service to docs. PR #1726 by @windson.
  * Add link to Starlette docs about WebSocket testing. PR #1717 by @hellocoldworld.
  * Refactor generating dependant, merge for loops. PR #1714 by @Bloodielie.
  * Update example for templates with Jinja to include HTML media type. PR #1690 by @frafra.
  * Fix typos in docs for security. PR #1678 by @nilslindemann.
  * Fix typos in docs for dependencies. PR #1675 by @nilslindemann.
  * Fix type annotation for `**extra` parameters in `FastAPI`. PR #1659 by @bharel.
  * Bump MkDocs Material to fix docs in browsers with dark mode. PR #1789 by @adriencaccia.
  * Remove docs preview comment from each commit. PR #1826.
  * Update GitHub context extraction for Gitter notification bot. PR #1766.


## 0.60.1¶
  * Add debugging logs for GitHub actions to introspect GitHub hidden context. PR #1764.
  * Use OS preference theme for online docs. PR #1760 by @adriencaccia.
  * Upgrade Starlette to version `0.13.6` to handle a vulnerability when using static files in Windows. PR #1759 by @jamesag26.
  * Pin Swagger UI temporarily, waiting for a fix for swagger-api/swagger-ui#6249. PR #1763.
  * Update GitHub Actions, use commit from PR for docs preview, not commit from pre-merge. PR #1761.
  * Update GitHub Actions, refactor Gitter bot. PR #1746.


## 0.60.0¶
  * Add GitHub Action to watch for missing preview docs and trigger a preview deploy. PR #1740.
  * Add custom GitHub Action to get artifact with docs preview. PR #1739.
  * Add new GitHub Actions to preview docs from PRs. PR #1738.
  * Add XML test coverage to support GitHub Actions. PR #1737.
  * Update badges and remove Travis now that GitHub Actions is the main CI. PR #1736.
  * Add GitHub Actions for CI, move from Travis. PR #1735.
  * Add support for adding OpenAPI schema for GET requests with a body. PR #1626 by @victorphoenix3.


## 0.59.0¶
  * Fix typo in docstring for OAuth2 utils. PR #1621 by @tomarv2.
  * Update JWT docs to use Python-jose instead of PyJWT. Initial PR #1610 by @asheux.
  * Fix/re-enable search bar in docs. PR #1703.
  * Auto-generate a "server" in OpenAPI `servers` when there's a `root_path` instead of prefixing all the `paths`:
    * Add a new parameter for `FastAPI` classes: `root_path_in_servers` to disable the auto-generation of `servers`.
    * New docs about `root_path` and `servers` in Additional Servers.
    * Update OAuth2 examples to use a relative URL for `tokenUrl="token"` to make sure those examples keep working as-is even when behind a reverse proxy.
    * Initial PR #1596 by @rkbeatss.
  * Fix typo/link in External Links. PR #1702.
  * Update handling of External Links to use a data file and allow translating the headers without becoming obsolete quickly when new links are added. PR #https://github.com/tiangolo/fastapi/pull/1701.
  * Add external link Machine learning model serving in Python using FastAPI and Streamlit to docs. PR #1669 by @davidefiocco.
  * Add note in docs on order in Pydantic Unions. PR #1591 by @kbanc.
  * Improve support for tests in editor. PR #1699.
  * Pin dependencies. PR #1697.
  * Update isort to version 5.x.x. PR #1670 by @asheux.


## 0.58.1¶
  * Add link in docs to Pydantic data types. PR #1612 by @tayoogunbiyi.
  * Fix link in warning logs for `openapi_prefix`. PR #1611 by @bavaria95.
  * Fix bad link in docs. PR #1603 by @molto0504.
  * Add Vim temporary files to `.gitignore` for contributors using Vim. PR #1590 by @asheux.
  * Fix typo in docs for sub-applications. PR #1578 by @schlpbch.
  * Use `Optional` in all the examples in the docs. Original PR #1574 by @chrisngyn, @kx-chen, @YKo20010. Updated and merged PR #1644.
  * Update tests and handling of `response_model_by_alias`. PR #1642.
  * Add translation to Chinese for Body - Fields - 请求体 - 字段. PR #1569 by @waynerv.
  * Update Chinese translation of main page. PR #1564 by @waynerv.
  * Add translation to Chinese for Body - Multiple Parameters - 请求体 - 多个参数. PR #1532 by @waynerv.
  * Add translation to Chinese for Path Parameters and Numeric Validations - 路径参数和数值校验. PR #1506 by @waynerv.
  * Add GitHub action to auto-label approved PRs (mainly for translations). PR #1638.


## 0.58.0¶
  * Deep merge OpenAPI responses to preserve all the additional metadata. PR #1577.
  * Mention in docs that only main app events are run (not sub-apps). PR #1554 by @amacfie.
  * Fix body validation error response, do not include body variable when it is not embedded. PR #1553 by @amacfie.
  * Fix testing OAuth2 security scopes when using dependency overrides. PR #1549 by @amacfie.
  * Fix Model for JSON Schema keyword `not` as a JSON Schema instead of a list. PR #1548 by @v-do.
  * Add support for OpenAPI `servers`. PR #1547 by @mikaello.


## 0.57.0¶
  * Remove broken link from "External Links". PR #1565 by @victorphoenix3.
  * Update/fix docs for WebSockets with dependencies. Original PR #1540 by @ChihSeanHsu.
  * Add support for Python's `http.HTTPStatus` in `status_code` parameters. PR #1534 by @retnikt.
  * When using Pydantic models with `__root__`, use the internal value in `jsonable_encoder`. PR #1524 by @patrickkwang.
  * Update docs for path parameters. PR #1521 by @yankeexe.
  * Update docs for first steps, links and rewording. PR #1518 by @yankeexe.
  * Enable `showCommonExtensions` in Swagger UI to show additional validations like `maxLength`, etc. PR #1466 by @TiewKH.
  * Make `OAuth2PasswordRequestFormStrict` importable directly from `fastapi.security`. PR #1462 by @RichardHoekstra.
  * Add docs about Default response class. PR #1455 by @TezRomacH.
  * Add note in docs about additional parameters `response_model_exclude_defaults` and `response_model_exclude_none` in Response Model. PR #1427 by @wshayes.
  * Add note about PyCharm Pydantic plugin to docs. PR #1420 by @koxudaxi.
  * Update and clarify testing function name. PR #1395 by @chenl.
  * Fix duplicated headers created by indirect dependencies that use the request directly. PR #1386 by @obataku from tests by @scottsmith2gmail.
  * Upgrade Starlette version to `0.13.4`. PR #1361 by @rushton.
  * Improve error handling and feedback for requests with invalid JSON. PR #1354 by @aviramha.
  * Add support for declaring metadata for tags in OpenAPI. New docs at Tutorial - Metadata and Docs URLs - Metadata for tags. PR #1348 by @thomas-maschler.
  * Add basic setup for Russian translations. PR #1566.
  * Remove obsolete Chinese articles after adding official community translations. PR #1510 by @waynerv.
  * Add `__repr__` for _path operation function_ parameter helpers (like `Query`, `Depends`, etc) to simplify debugging. PR #1560 by @rkbeatss and @victorphoenix3.


## 0.56.1¶
  * Add link to advanced docs from tutorial. PR #1512 by @kx-chen.
  * Remove internal unnecessary f-strings. PR #1526 by @kotamatsuoka.
  * Add translation to Chinese for Query Parameters and String Validations - 查询参数和字符串校验. PR #1500 by @waynerv.
  * Add translation to Chinese for Request Body - 请求体. PR #1492 by @waynerv.
  * Add translation to Chinese for Help FastAPI - Get Help - 帮助 FastAPI - 获取帮助. PR #1465 by @waynerv.
  * Add translation to Chinese for Query Parameters - 查询参数. PR #1454 by @waynerv.
  * Add translation to Chinese for Contributing - 开发 - 贡献. PR #1460 by @waynerv.
  * Add translation to Chinese for Path Parameters - 路径参数. PR #1453 by @waynerv.
  * Add official Microsoft project generator for serving spaCy with FastAPI and Azure Cognitive Skills to Project Generators. PR #1390 by @kabirkhan.
  * Update docs in Python Types Intro to include info about `Optional`. Original PR #1377 by @yaegassy.
  * Fix support for callable class dependencies with `yield`. PR #1365 by @mrosales.
  * Fix/remove incorrect error logging when a client sends invalid payloads. PR #1351 by @dbanty.
  * Add translation to Chinese for First Steps - 第一步. PR #1323 by @waynerv.
  * Fix generating OpenAPI for apps using callbacks with routers including Pydantic models. PR #1322 by @nsidnev.
  * Optimize internal regex performance in `get_path_param_names()`. PR #1243 by @heckad.
  * Remove `*,` from functions in docs where it's not needed. PR #1239 by @pankaj-giri.
  * Start translations for Italian. PR #1557 by @csr.


## 0.56.0¶
  * Add support for ASGI `root_path`:
    * Use `root_path` internally for mounted applications, so that OpenAPI and the docs UI works automatically without extra configurations and parameters.
    * Add new `root_path` parameter for `FastAPI` applications to provide it in cases where it can be set with the command line (e.g. for Uvicorn and Hypercorn, with the parameter `--root-path`).
    * Deprecate `openapi_prefix` parameter in favor of the new `root_path` parameter.
    * Add new/updated docs for Sub Applications - Mounts, without `openapi_prefix` (as it is now handled automatically).
    * Add new/updated docs for Behind a Proxy, including how to setup a local testing proxy with Traefik and using `root_path`.
    * Update docs for Extending OpenAPI with the new `openapi_prefix` parameter passed (internally generated from `root_path`).
    * Original PR #1199 by @iksteen.
  * Update new issue templates and docs: Help FastAPI - Get Help. PR #1531.
  * Update GitHub action issue-manager. PR #1520.
  * Add new links:
    * **English articles** :
      * Real-time Notifications with Python and Postgres by Guillermo Cruz.
      * Microservice in Python using FastAPI by Paurakh Sharma Humagain.
      * Build simple API service with Python FastAPI — Part 1 by cuongld2.
      * FastAPI + Zeit.co = 🚀 by Paul Sec.
      * Build a web API from scratch with FastAPI - the workshop by Sebastián Ramírez (tiangolo).
      * Build a Secure Twilio Webhook with Python and FastAPI by Twilio.
      * Using FastAPI with Django by Stavros Korokithakis.
      * Introducing Dispatch by Netflix.
    * **Podcasts** :
      * Build The Next Generation Of Python Web Applications With FastAPI - Episode 259 - interview to Sebastían Ramírez (tiangolo) by Podcast.`__init__`.
    * **Talks** :
      * PyConBY 2020: Serve ML models easily with FastAPI by Sebastián Ramírez (tiangolo).
      * [VIRTUAL] Py.Amsterdam's flying Software Circus: Intro to FastAPI by Sebastián Ramírez (tiangolo).
    * PR #1467.
  * Add translation to Chinese for Python Types Intro - Python 类型提示简介. PR #1197 by @waynerv.


## 0.55.1¶
  * Fix handling of enums with their own schema in path parameters. To support pydantic/pydantic#1432 in FastAPI. PR #1463.


## 0.55.0¶
  * Allow enums to allow them to have their own schemas in OpenAPI. To support pydantic/pydantic#1432 in FastAPI. PR #1461.
  * Add links for funding through GitHub sponsors. PR #1425.
  * Update issue template for for questions. PR #1344 by @retnikt.
  * Update warning about storing passwords in docs. PR #1336 by @skorokithakis.
  * Fix typo. PR #1326 by @chenl.
  * Add translation to Portuguese for Alternatives, Inspiration and Comparisons - Alternativas, Inspiração e Comparações. PR #1325 by @Serrones.
  * Fix 2 typos in docs. PR #1324 by @waynerv.
  * Update CORS docs, fix correct default of `max_age=600`. PR #1301 by @derekbekoe.
  * Add translation of main page to Portuguese. PR #1300 by @Serrones.
  * Re-word and clarify docs for extra info in fields. PR #1299 by @chris-allnutt.
  * Make sure the `*` in short features in the docs is consistent (after `.`) in all languages. PR #1424.
  * Update order of execution for `get_db` in SQLAlchemy tutorial. PR #1293 by @bcb.
  * Fix typos in Async docs. PR #1423.


## 0.54.2¶
  * Add translation to Spanish for Concurrency and async / await - Concurrencia y async / await. PR #1290 by @alvaropernas.
  * Remove obsolete vote link. PR #1289 by @donhui.
  * Allow disabling docs UIs by just disabling OpenAPI with `openapi_url=None`. New example in docs: Advanced: Conditional OpenAPI. PR #1421.
  * Add translation to Portuguese for Benchmarks - Comparações. PR #1274 by @Serrones.
  * Add translation to Portuguese for Tutorial - User Guide - Intro - Tutorial - Guia de Usuário - Introdução. PR #1259 by @marcosmmb.
  * Allow using Unicode in MkDocs for translations. PR #1419.
  * Add translation to Spanish for Advanced User Guide - Intro - Guía de Usuario Avanzada - Introducción. PR #1250 by @jfunez.
  * Add translation to Portuguese for History, Design and Future - História, Design e Futuro. PR #1249 by @marcosmmb.
  * Add translation to Portuguese for Features - Recursos. PR #1248 by @marcosmmb.
  * Add translation to Spanish for Tutorial - User Guide - Intro - Tutorial - Guía de Usuario - Introducción. PR #1244 by @MartinEliasQ.
  * Add translation to Chinese for Deployment - 部署. PR #1203 by @RunningIkkyu.
  * Add translation to Chinese for Tutorial - User Guide - Intro - 教程 - 用户指南 - 简介. PR #1202 by @waynerv.
  * Add translation to Chinese for Features - 特性. PR #1192 by @Dustyposa.
  * Add translation for main page to Chinese PR #1191 by @waynerv.
  * Update docs for project generation. PR #1287.
  * Add Spanish translation for Introducción a los Tipos de Python (Python Types Intro). PR #1237 by @mariacamilagl.
  * Add Spanish translation for Características (Features). PR #1220 by @mariacamilagl.


## 0.54.1¶
  * Update database test setup. PR #1226.
  * Improve test debugging by showing response text in failing tests. PR #1222 by @samuelcolvin.


## 0.54.0¶
  * Fix grammatical mistakes in async docs. PR #1188 by @mickeypash.
  * Add support for `response_model_exclude_defaults` and `response_model_exclude_none`:
    * Deprecate the parameter `include_none` in `jsonable_encoder` and add the inverted `exclude_none`, to keep in sync with Pydantic.
    * PR #1166 by @voegtlel.
  * Add example about Testing a Database. Initial PR #1144 by @duganchen.
  * Update docs for Development - Contributing: Translations including note about reviewing translation PRs. #1215.
  * Update log style in README.md for GitHub Markdown compatibility. PR #1200 by #geekgao.
  * Add Python venv `env` to `.gitignore`. PR #1212 by @cassiobotaro.
  * Start Portuguese translations. PR #1210 by @cassiobotaro.
  * Update docs for Pydantic's `Settings` using a dependency with `@lru_cache()`. PR #1214.
  * Add first translation to Spanish FastAPI. PR #1201 by @mariacamilagl.
  * Add docs about Settings and Environment Variables. Initial PR 1118 by @alexmitelman.


## 0.53.2¶
  * Fix automatic embedding of body fields for dependencies and sub-dependencies. Original PR #1079 by @Toad2186.
  * Fix dependency overrides in WebSocket testing. PR #1122 by @amitlissack.
  * Fix docs script to ensure languages are always sorted. PR #1189.
  * Start translations for Chinese. PR #1187 by @RunningIkkyu.
  * Add docs for Schema Extra - Example. PR #1185.


## 0.53.1¶
  * Fix included example after translations refactor. PR #1182.
  * Add docs example for `example` in `Field`. Docs at Body - Fields: JSON Schema extras. PR #1106 by @JohnPaton.
  * Fix using recursive models in `response_model`. PR #1164 by @voegtlel.
  * Add docs for Pycharm Debugging. PR #1096 by @youngquan.
  * Fix typo in docs. PR #1148 by @PLNech.
  * Update Windows development environment instructions. PR #1179.


## 0.53.0¶
  * Update test coverage badge. PR #1175.
  * Add `orjson` to `pip install fastapi[all]`. PR #1161 by @michael0liver.
  * Fix included example for `GZipMiddleware`. PR #1138 by @arimbr.
  * Fix class name in docstring for `OAuth2PasswordRequestFormStrict`. PR #1126 by @adg-mh.
  * Clarify function name in example in docs. PR #1121 by @tmsick.
  * Add external link Apache Kafka producer and consumer with FastAPI and aiokafka to docs. PR #1112 by @iwpnd.
  * Fix serialization when using `by_alias` or `exclude_unset` and returning data with Pydantic models. PR #1074 by @juhovh-aiven.
  * Add Gitter chat to docs. PR #1061 by @aakashnand.
  * Update and simplify translations docs. PR #1171.
  * Update development of FastAPI docs, set address to `127.0.0.1` to improve Windows support. PR #1169 by @mariacamilagl.
  * Add support for docs translations. New docs: Development - Contributing: Docs: Translations. PR #1168.
  * Update terminal styles in docs and add note about **Typer** , the FastAPI of CLIs. PR #1139.


## 0.52.0¶
  * Add new high-performance JSON response class using `orjson`. New docs: Custom Response - HTML, Stream, File, others: `ORJSONResponse`. PR #1065.


## 0.51.0¶
  * Re-export utils from Starlette:
    * This allows using things like `from fastapi.responses import JSONResponse` instead of `from starlette.responses import JSONResponse`.
    * It's mainly syntax sugar, a convenience for developer experience.
    * Now `Request`, `Response`, `WebSocket`, `status` can be imported directly from `fastapi` as in `from fastapi import Response`. This is because those are frequently used, to use the request directly, to set headers and cookies, to get status codes, etc.
    * Documentation changes in many places, but new docs and noticeable improvements:
      * Custom Response - HTML, Stream, File, others.
      * Advanced Middleware.
      * Including WSGI - Flask, Django, others.
    * PR #1064.


## 0.50.0¶
  * Add link to Release Notes from docs about pinning versions for deployment. PR #1058.
  * Upgrade code to use the latest version of Starlette, including:
    * Several bug fixes.
    * Optional redirects of slashes, with or without ending in `/`.
    * Events for routers, `"startup"`, and `"shutdown"`.
    * PR #1057.
  * Add docs about pinning FastAPI versions for deployment: Deployment: FastAPI versions. PR #1056.


## 0.49.2¶
  * Fix links in release notes. PR #1052 by @sattosan.
  * Fix typo in release notes. PR #1051 by @sattosan.
  * Refactor/clarify `serialize_response` parameter name to avoid confusion. PR #1031 by @patrickmckenna.
  * Refactor calling each a path operation's handler function in an isolated function, to simplify profiling. PR #1027 by @sm-Fifteen.
  * Add missing dependencies for testing. PR #1026 by @sm-Fifteen.
  * Fix accepting valid types for response models, including Python types like `List[int]`. PR #1017 by @patrickmckenna.
  * Fix format in SQL tutorial. PR #1015 by @vegarsti.


## 0.49.1¶
  * Fix path operation duplicated parameters when used in dependencies and the path operation function. PR #994 by @merowinger92.
  * Update Netlify previews deployment GitHub action as the fix is already merged and there's a new release. PR #1047.
  * Move mypy configurations to config file. PR #987 by @hukkinj1.
  * Temporary fix to Netlify previews not deployable from PRs from forks. PR #1046 by @mariacamilagl.


## 0.49.0¶
  * Fix encoding of `pathlib` paths in `jsonable_encoder`. PR #978 by @patrickmckenna.
  * Add articles to External Links: PythonのWeb frameworkのパフォーマンス比較 (Django, Flask, responder, FastAPI, japronto) and [FastAPI] Python製のASGI Web フレームワーク FastAPIに入門する. PR #974 by @tokusumi.
  * Fix broken links in docs. PR #949 by @tsotnikov.
  * Fix small typos. PR #941 by @NikitaKolesov.
  * Update and clarify docs for dependencies with `yield`. PR #986.
  * Add Mermaid JS support for diagrams in docs. Add first diagrams to Dependencies: First Steps and Dependencies with `yield` and `HTTPException`. PR #985.
  * Update CI to run docs deployment in GitHub actions. PR #983.
  * Allow `callable`s in _path operation functions_ , like functions modified with `functools.partial`. PR #977.


## 0.48.0¶
  * Run linters first in tests to error out faster. PR #948.
  * Log warning about `email-validator` only when used. PR #946.
  * Simplify Peewee docs with double dependency with `yield`. PR #947.
  * Add article External Links: Create and Deploy FastAPI app to Heroku. PR #942 by @windson.
  * Update description of Sanic, as it is now ASGI too. PR #932 by @raphaelauv.
  * Fix typo in main page. PR #920 by @mMarzeta.
  * Fix parsing of possibly invalid bodies. PR #918 by @dmontagu.
  * Fix typo #916 by @adursun.
  * Allow `Any` type for enums in OpenAPI. PR #906 by @songzhi.
  * Add article to External Links: How to continuously deploy a FastAPI to AWS Lambda with AWS SAM. PR #901 by @iwpnd.
  * Add note about using Body parameters without Pydantic. PR #900 by @pawamoy.
  * Fix Pydantic field clone logic. PR #899 by @deuce2367.
  * Fix link in middleware docs. PR #893 by @linchiwei123.
  * Rename default API title from "Fast API" to "FastAPI" for consistency. PR #890.


## 0.47.1¶
  * Fix model filtering in `response_model`, cloning sub-models. PR #889.
  * Fix FastAPI serialization of Pydantic models using ORM mode blocking the event loop. PR #888.


## 0.47.0¶
  * Refactor documentation to make a simpler and shorter Tutorial - User Guide and an additional Advanced User Guide with all the additional docs. PR #887.
  * Tweak external links, Markdown format, typos. PR #881.
  * Fix bug in tutorial handling HTTP Basic Auth `username` and `password`. PR #865 by @isaevpd.
  * Fix handling form _path operation_ parameters declared with pure classes like `list`, `tuple`, etc. PR #856 by @nsidnev.
  * Add request `body` to `RequestValidationError`, new docs: Use the `RequestValidationError` body. Initial PR #853 by @aviramha.
  * Update External Links with new links and dynamic GitHub projects with `fastapi` topic. PR #850.
  * Fix Peewee `contextvars` handling in docs: SQL (Relational) Databases with Peewee. PR #879.
  * Setup development environment with Python's Venv and Flit, instead of requiring the extra Pipenv duplicating dependencies. Updated docs: Development - Contributing. PR #877.
  * Update docs for HTTP Basic Auth to improve security against timing attacks. Initial PR #807 by @zwass.


## 0.46.0¶
  * Fix typos and tweak configs. PR #837.
  * Add link to Chinese article in External Links. PR 810 by @wxq0309.
  * Implement `OAuth2AuthorizationCodeBearer` class. PR #797 by @kuwv.
  * Update example upgrade in docs main page. PR #795 by @cdeil.
  * Fix callback handling for sub-routers. PR #792 by @jekirl.
  * Fix typos. PR #784 by @kkinder.
  * Add 4 Japanese articles to External Links. PR #783 by @HymanZHAN.
  * Add support for subtypes of main types in `jsonable_encoder`, e.g. asyncpg's UUIDs. PR #756 by @RmStorm.
  * Fix usage of Pydantic's `HttpUrl` in docs. PR #832 by @Dustyposa.
  * Fix Twitter links in docs. PR #813 by @justindujardin.
  * Add docs for correctly using FastAPI with Peewee ORM. Including how to overwrite parts of Peewee to correctly handle async threads. PR #789.


## 0.45.0¶
  * Add support for OpenAPI Callbacks:
    * New docs: OpenAPI Callbacks.
    * Refactor generation of `operationId`s to be valid Python names (also valid variables in most languages).
    * Add `default_response_class` parameter to `APIRouter`.
    * Original PR #722 by @booooh.
  * Refactor logging to use the same logger everywhere, update log strings and levels. PR #781.
  * Add article to External Links: Почему Вы должны попробовать FastAPI?. PR #766 by @prostomarkeloff.
  * Remove gender bias in docs for handling errors. PR #780. Original idea in PR #761 by @classywhetten.
  * Rename docs and references to `body-schema` to `body-fields` to keep in line with Pydantic. PR #746 by @prostomarkeloff.


## 0.44.1¶
  * Add GitHub social preview images to git. PR #752.
  * Update PyPI "trove classifiers". PR #751.
  * Add full support for Python 3.8. Enable Python 3.8 in full in Travis. PR 749.
  * Update "new issue" templates. PR #749.
  * Fix serialization of errors for exotic Pydantic types. PR #748 by @dmontagu.


## 0.44.0¶
  * Add GitHub action Issue Manager. PR #742.
  * Fix typos in docs. PR 734 by @bundabrg.
  * Fix usage of `custom_encoder` in `jsonable_encoder`. PR #715 by @matrixise.
  * Fix invalid XML example. PR 710 by @OcasoProtal.
  * Fix typos and update wording in deployment docs. PR #700 by @marier-nico.
  * Add note about dependencies in `APIRouter` docs. PR #698 by @marier-nico.
  * Add support for async class methods as dependencies #681 by @frankie567.
  * Add FastAPI with Swagger UI cheatsheet to external links. PR #671 by @euri10.
  * Fix typo in HTTP protocol in CORS example. PR #647 by @forestmonster.
  * Add support for Pydantic versions `1.0.0` and above, with temporary (deprecated) backwards compatibility for Pydantic `0.32.2`. PR #646 by @dmontagu.


## 0.43.0¶
  * Update docs to reduce gender bias. PR #645 by @ticosax.
  * Add docs about overriding the `operationId` for all the _path operations_ based on their function name. PR #642 by @SKalt.
  * Fix validators in models generating an incorrect key order. PR #637 by @jaddison.
  * Generate correct OpenAPI docs for responses with no content. PR #621 by @brotskydotcom.
  * Remove `$` from Bash code blocks in docs for consistency. PR #613 by @nstapelbroek.
  * Add docs for self-serving docs' (Swagger UI) static assets, e.g. to use the docs offline, or without Internet. Initial PR #557 by @svalouch.
  * Fix `black` linting after upgrade. PR #682 by @frankie567.


## 0.42.0¶
  * Add dependencies with `yield`, a.k.a. exit steps, context managers, cleanup, teardown, ...
    * This allows adding extra code after a dependency is done. It can be used, for example, to close database connections.
    * Dependencies with `yield` can be normal or `async`, **FastAPI** will run normal dependencies in a threadpool.
    * They can be combined with normal dependencies.
    * It's possible to have arbitrary trees/levels of dependencies with `yield` and exit steps are handled in the correct order automatically.
    * It works by default in Python 3.7 or above. For Python 3.6, it requires the extra backport dependencies:
      * `async-exit-stack`
      * `async-generator`
    * New docs at Dependencies with `yield`.
    * Updated database docs SQL (Relational) Databases: Main **FastAPI** app.
    * PR #595.
  * Fix `sitemap.xml` in website. PR #598 by @samuelcolvin.


## 0.41.0¶
  * Upgrade required Starlette to `0.12.9`, the new range is `>=0.12.9,<=0.12.9`.
    * Add `State` to FastAPI apps at `app.state`.
    * PR #593.
  * Improve handling of custom classes for `Request`s and `APIRoute`s.
    * This helps to more easily solve use cases like:
      * Reading a body before and/or after a request (equivalent to a middleware).
      * Run middleware-like code only for a subset of _path operations_.
      * Process a request before passing it to a _path operation function_. E.g. decompressing, deserializing, etc.
      * Processing a response after being generated by _path operation functions_ but before returning it. E.g. adding custom headers, logging, adding extra metadata.
    * New docs section: Custom Request and APIRoute class.
    * PR #589 by @dmontagu.
  * Fix preserving custom route class in routers when including other sub-routers. PR #538 by @dmontagu.


## 0.40.0¶
  * Add notes to docs about installing `python-multipart` when using forms. PR #574 by @sliptonic.
  * Generate OpenAPI schemas in alphabetical order. PR #554 by @dmontagu.
  * Add support for truncating docstrings from _path operation functions_.
    * New docs at Advanced description from docstring.
    * PR #556 by @svalouch.
  * Fix `DOCTYPE` in HTML files generated for Swagger UI and ReDoc. PR #537 by @Trim21.
  * Fix handling `4XX` responses overriding default `422` validation error responses. PR #517 by @tsouvarev.
  * Fix typo in documentation for Simple HTTP Basic Auth. PR #514 by @prostomarkeloff.
  * Fix incorrect documentation example in first steps. PR #511 by @IgnatovFedor.
  * Add support for Swagger UI initOauth settings with the parameter `swagger_ui_init_oauth`. PR #499 by @zamiramir.


## 0.39.0¶
  * Allow path parameters to have default values (e.g. `None`) and discard them instead of raising an error.
    * This allows declaring a parameter like `user_id: str = None` that can be taken from a query parameter, but the same _path operation_ can be included in a router with a path `/users/{user_id}`, in which case will be taken from the path and will be required.
    * PR #464 by @jonathanunderwood.
  * Add support for setting a `default_response_class` in the `FastAPI` instance or in `include_router`. Initial PR #467 by @toppk.
  * Add support for type annotations using strings and `from __future__ import annotations`. PR #451 by @dmontagu.


## 0.38.1¶
  * Fix incorrect `Request` class import. PR #493 by @kamalgill.


## 0.38.0¶
  * Add recent articles to External Links and recent opinions. PR #490.
  * Upgrade support range for Starlette to include `0.12.8`. The new range is `>=0.11.1,<=0.12.8"`. PR #477 by @dmontagu.
  * Upgrade support to Pydantic version 0.32.2 and update internal code to use it (breaking change). PR #463 by @dmontagu.


## 0.37.0¶
  * Add support for custom route classes for advanced use cases. PR #468 by @dmontagu.
  * Allow disabling Google fonts in ReDoc. PR #481 by @b1-luettje.
  * Fix security issue: when returning a sub-class of a response model and using `skip_defaults` it could leak information. PR #485 by @dmontagu.
  * Enable tests for Python 3.8-dev. PR #465 by @Jamim.
  * Add support and tests for Pydantic dataclasses in `response_model`. PR #454 by @dconathan.
  * Fix typo in OAuth2 JWT tutorial. PR #447 by @pablogamboa.
  * Use the `media_type` parameter in `Body()` params to set the media type in OpenAPI for `requestBody`. PR #439 by @divums.
  * Add article Deploying a scikit-learn model with ONNX and FastAPI by Nico Axtmann. PR #438 by @naxty.
  * Allow setting custom `422` (validation error) response/schema in OpenAPI.
    * And use media type from response class instead of fixed `application/json` (the default).
    * PR #437 by @divums.
  * Fix using `"default"` extra response with status codes at the same time. PR #489.
  * Allow additional responses to use status code ranges (like `5XX` and `4XX`) and `"default"`. PR #435 by @divums.


## 0.36.0¶
  * Fix implementation for `skip_defaults` when returning a Pydantic model. PR #422 by @dmontagu.
  * Fix OpenAPI generation when using the same dependency in multiple places for the same _path operation_. PR #417 by @dmontagu.
  * Allow having empty paths in _path operations_ used with `include_router` and a `prefix`.
    * This allows having a router for `/cats` and all its _path operations_ , while having one of them for `/cats`.
    * Now it doesn't have to be only `/cats/` (with a trailing slash).
    * To use it, declare the path in the _path operation_ as the empty string (`""`).
    * PR #415 by @vitalik.
  * Fix mypy error after merging PR #415. PR #462.


## 0.35.0¶
  * Fix typo in routing `assert`. PR #419 by @pablogamboa.
  * Fix typo in docs. PR #411 by @bronsen.
  * Fix parsing a body type declared with `Union`. PR #400 by @koxudaxi.


## 0.34.0¶
  * Upgrade Starlette supported range to include the latest `0.12.7`. The new range is `0.11.1,<=0.12.7`. PR #367 by @dedsm.
  * Add test for OpenAPI schema with duplicate models from PR #333 by @dmontagu. PR #385.


## 0.33.0¶
  * Upgrade Pydantic version to `0.30.0`. PR #384 by @jekirl.


## 0.32.0¶
  * Fix typo in docs for features. PR #380 by @MartinoMensio.
  * Fix source code `limit` for example in Query Parameters. PR #366 by @Smashman.
  * Update wording in docs about OAuth2 scopes. PR #371 by @cjw296.
  * Update docs for `Enum`s to inherit from `str` and improve Swagger UI rendering. PR #351.
  * Fix regression, add Swagger UI deep linking again. PR #350.
  * Add test for having path templates in `prefix` of `.include_router`. PR #349.
  * Add note to docs: Include the same router multiple times with different `prefix`. PR #348.
  * Fix OpenAPI/JSON Schema generation for two functions with the same name (in different modules) with the same composite bodies.
    * Composite bodies' IDs are now based on path, not only on route name, as the auto-generated name uses the function names, that can be duplicated in different modules.
    * The same new ID generation applies to response models.
    * This also changes the generated title for those models.
    * Only composite bodies and response models are affected because those are generated dynamically, they don't have a module (a Python file).
    * This also adds the possibility of using `.include_router()` with the same `APIRouter` _multiple_ times, with different prefixes, e.g. `/api/v2` and `/api/latest`, and it will now work correctly.
    * PR #347.


## 0.31.0¶
  * Upgrade Pydantic supported version to `0.29.0`.
    * New supported version range is `"pydantic >=0.28,<=0.29.0"`.
    * This adds support for Pydantic Generic Models, kudos to @dmontagu.
    * PR #344.


## 0.30.1¶
  * Add section in docs about External Links and Articles. PR #341.
  * Remove `Pipfile.lock` from the repository as it is only used by FastAPI contributors (developers of FastAPI itself). See the PR for more details. PR #340.
  * Update section about Help FastAPI - Get Help. PR #339.
  * Refine internal type declarations to improve/remove Mypy errors in users' code. PR #338.
  * Update and clarify SQL tutorial with SQLAlchemy. PR #331 by @mariacamilagl.
  * Add SQLite online viewers to the docs. PR #330 by @cyrilbois.


## 0.30.0¶
  * Add support for Pydantic's ORM mode:
    * Updated documentation about SQL with SQLAlchemy, using Pydantic models with ORM mode, SQLAlchemy models with relations, separation of files, simplification of code and other changes. New docs: SQL (Relational) Databases.
    * The new support for ORM mode fixes issues/adds features related to ORMs with lazy-loading, hybrid properties, dynamic/getters (using `@property` decorators) and several other use cases.
    * This applies to ORMs like SQLAlchemy, Peewee, Tortoise ORM, GINO ORM and virtually any other.
    * If your _path operations_ return an arbitrary object with attributes (e.g. `my_item.name` instead of `my_item["name"]`) AND you use a `response_model`, make sure to update the Pydantic models with `orm_mode = True` as described in the docs (link above).
    * New documentation about receiving plain `dict`s as request bodies: Bodies of arbitrary `dict`s.
    * New documentation about returning arbitrary `dict`s in responses: Response with arbitrary `dict`.
    * **Technical Details** :
      * When declaring a `response_model` it is used directly to generate the response content, from whatever was returned from the _path operation function_.
      * Before this, the return content was first passed through `jsonable_encoder` to ensure it was a "jsonable" object, like a `dict`, instead of an arbitrary object with attributes (like an ORM model). That's why you should make sure to update your Pydantic models for objects with attributes to use `orm_mode = True`.
      * If you don't have a `response_model`, the return object will still be passed through `jsonable_encoder` first.
      * When a `response_model` is declared, the same `response_model` type declaration won't be used as is, it will be "cloned" to create an new one (a cloned Pydantic `Field` with all the submodels cloned as well).
      * This avoids/fixes a potential security issue: as the returned object is passed directly to Pydantic, if the returned object was a subclass of the `response_model` (e.g. you return a `UserInDB` that inherits from `User` but contains extra fields, like `hashed_password`, and `User` is used in the `response_model`), it would still pass the validation (because `UserInDB` is a subclass of `User`) and the object would be returned as-is, including the `hashed_password`. To fix this, the declared `response_model` is cloned, if it is a Pydantic model class (or contains Pydantic model classes in it, e.g. in a `List[Item]`), the Pydantic model class(es) will be a different one (the "cloned" one). So, an object that is a subclass won't simply pass the validation and returned as-is, because it is no longer a sub-class of the cloned `response_model`. Instead, a new Pydantic model object will be created with the contents of the returned object. So, it will be a new object (made with the data from the returned one), and will be filtered by the cloned `response_model`, containing only the declared fields as normally.
    * PR #322.
  * Remove/clean unused RegEx code in routing. PR #314 by @dmontagu.
  * Use default response status code descriptions for additional responses. PR #313 by @duxiaoyao.
  * Upgrade Pydantic support to `0.28`. PR #320 by @jekirl.


## 0.29.1¶
  * Fix handling an empty-body request with a required body param. PR #311.
  * Fix broken link in docs: Return a Response directly. PR #306 by @dmontagu.
  * Fix docs discrepancy in docs for Response Model. PR #288 by @awiddersheim.


## 0.29.0¶
  * Add support for declaring a `Response` parameter:
    * This allows declaring:
      * Response Cookies.
      * Response Headers.
      * An HTTP Status Code different than the default: Response - Change Status Code.
    * All of this while still being able to return arbitrary objects (`dict`, DB model, etc).
    * Update attribution to Hug, for inspiring the `response` parameter pattern.
    * PR #294.


## 0.28.0¶
  * Implement dependency cache per request.
    * This avoids calling each dependency multiple times for the same request.
    * This is useful while calling external services, performing costly computation, etc.
    * This also means that if a dependency was declared as a _path operation decorator_ dependency, possibly at the router level (with `.include_router()`) and then it is declared again in a specific _path operation_ , the dependency will be called only once.
    * The cache can be disabled per dependency declaration, using `use_cache=False` as in `Depends(your_dependency, use_cache=False)`.
    * Updated docs at: Using the same dependency multiple times.
    * PR #292.
  * Implement dependency overrides for testing.
    * This allows using overrides/mocks of dependencies during tests.
    * New docs: Testing Dependencies with Overrides.
    * PR #291.


## 0.27.2¶
  * Fix path and query parameters receiving `dict` as a valid type. It should be mapped to a body payload. PR #287. Updated docs at: Query parameter list / multiple values with defaults: Using `list`.


## 0.27.1¶
  * Fix `auto_error=False` handling in `HTTPBearer` security scheme. Do not `raise` when there's an incorrect `Authorization` header if `auto_error=False`. PR #282.
  * Fix type declaration of `HTTPException`. PR #279.


## 0.27.0¶
  * Fix broken link in docs about OAuth 2.0 with scopes. PR #275 by @dmontagu.
  * Refactor param extraction using Pydantic `Field`:
    * Large refactor, improvement, and simplification of param extraction from _path operations_.
    * Fix/add support for list _query parameters_ with list defaults. New documentation: Query parameter list / multiple values with defaults.
    * Add support for enumerations in _path operation_ parameters. New documentation: Path Parameters: Predefined values.
    * Add support for type annotations using `Optional` as in `param: Optional[str] = None`. New documentation: Optional type declarations.
    * PR #278.


## 0.26.0¶
  * Separate error handling for validation errors.
    * This will allow developers to customize the exception handlers.
    * Document better how to handle exceptions and use error handlers.
    * Include `RequestValidationError` and `WebSocketRequestValidationError` (this last one will be useful once encode/starlette#527 or equivalent is merged).
    * New documentation about exceptions handlers:
      * Install custom exception handlers.
      * Override the default exception handlers.
      * Reuse **FastAPI's** exception handlers.
    * PR #273.
  * Fix support for _paths_ in _path parameters_ without needing explicit `Path(...)`.
    * PR #256.
    * Documented in PR #272 by @wshayes.
    * New documentation at: Path Parameters containing paths.
  * Update docs for testing FastAPI. Include using `POST`, sending JSON, testing headers, etc. New documentation: Testing. PR #271.
  * Fix type declaration of `response_model` to allow generic Python types as `List[Model]`. Mainly to fix `mypy` for users. PR #266.


## 0.25.0¶
  * Add support for Pydantic's `include`, `exclude`, `by_alias`.
    * Update documentation: Response Model.
    * Add docs for: Body - updates, using Pydantic's `skip_defaults`.
    * Add method consistency tests.
    * PR #264.
  * Add `CONTRIBUTING.md` file to GitHub, to help new contributors. PR #255 by @wshayes.
  * Add support for Pydantic's `skip_defaults`:
    * There's a new _path operation decorator_ parameter `response_model_skip_defaults`.
      * The name of the parameter will most probably change in a future version to `response_skip_defaults`, `model_skip_defaults` or something similar.
    * New documentation section about using `response_model_skip_defaults`.
    * PR #248 by @wshayes.


## 0.24.0¶
  * Add support for WebSockets with dependencies and parameters.
    * Support included for:
      * `Depends`
      * `Security`
      * `Cookie`
      * `Header`
      * `Path`
      * `Query`
      * ...as these are compatible with the WebSockets protocol (e.g. `Body` is not).
    * Updated documentation for WebSockets.
    * PR #178 by @jekirl.
  * Upgrade the compatible version of Pydantic to `0.26.0`.
    * This includes JSON Schema support for IP address and network objects, bug fixes, and other features.
    * PR #247 by @euri10.


## 0.23.0¶
  * Upgrade the compatible version of Starlette to `0.12.0`.
    * This includes support for ASGI 3 (the latest version of the standard).
    * It's now possible to use Starlette's `StreamingResponse` with iterators, like file-like objects (as those returned by `open()`).
    * It's now possible to use the low level utility `iterate_in_threadpool` from `starlette.concurrency` (for advanced scenarios).
    * PR #243.
  * Add OAuth2 redirect page for Swagger UI. This allows having delegated authentication in the Swagger UI docs. For this to work, you need to add `{your_origin}/docs/oauth2-redirect` to the allowed callbacks in your OAuth2 provider (in Auth0, Facebook, Google, etc).
    * For example, during development, it could be `http://localhost:8000/docs/oauth2-redirect`.
    * Keep in mind that this callback URL is independent of whichever one is used by your frontend. You might also have another callback at `https://yourdomain.com/login/callback`.
    * This is only to allow delegated authentication in the API docs with Swagger UI.
    * PR #198 by @steinitzu.
  * Make Swagger UI and ReDoc route handlers (_path operations_) be `async` functions instead of lambdas to improve performance. PR #241 by @Trim21.
  * Make Swagger UI and ReDoc URLs parameterizable, allowing to host and serve local versions of them and have offline docs. PR #112 by @euri10.


## 0.22.0¶
  * Add support for `dependencies` parameter:
    * A parameter in _path operation decorators_ , for dependencies that should be executed but the return value is not important or not used in the _path operation function_.
    * A parameter in the `.include_router()` method of FastAPI applications and routers, to include dependencies that should be executed in each _path operation_ in a router.
      * This is useful, for example, to require authentication or permissions in specific group of _path operations_.
      * Different `dependencies` can be applied to different routers.
    * These `dependencies` are run before the normal parameter dependencies. And normal dependencies are run too. They can be combined.
    * Dependencies declared in a router are executed first, then the ones defined in _path operation decorators_ , and then the ones declared in normal parameters. They are all combined and executed.
    * All this also supports using `Security` with `scopes` in those `dependencies` parameters, for more advanced OAuth 2.0 security scenarios with scopes.
    * New documentation about dependencies in _path operation decorators_.
    * New documentation about dependencies in the `include_router()` method.
    * PR #235.
  * Fix OpenAPI documentation of Starlette URL convertors. Specially useful when using `path` convertors, to take a whole path as a parameter, like `/some/url/{p:path}`. PR #234 by @euri10.
  * Make default parameter utilities exported from `fastapi` be functions instead of classes (the new functions return instances of those classes). To be able to override the return types and fix `mypy` errors in FastAPI's users' code. Applies to `Path`, `Query`, `Header`, `Cookie`, `Body`, `Form`, `File`, `Depends`, and `Security`. PR #226 and PR #231.
  * Separate development scripts `test.sh`, `lint.sh`, and `format.sh`. PR #232.
  * Re-enable `black` formatting checks for Python 3.7. PR #229 by @zamiramir.


## 0.21.0¶
  * On body parsing errors, raise `from` previous exception, to allow better introspection in logging code. PR #192 by @ricardomomm.
  * Use Python logger named "`fastapi`" instead of root logger. PR #222 by @euri10.
  * Upgrade Pydantic to version 0.25. PR #225 by @euri10.
  * Fix typo in routing. PR #221 by @djlambert.


## 0.20.1¶
  * Add typing information to package including file `py.typed`. PR #209 by @meadsteve.
  * Add FastAPI bot for Gitter. To automatically announce new releases. PR #189.


## 0.20.0¶
  * Upgrade OAuth2:
    * Upgrade Password flow using Bearer tokens to use the correct HTTP status code 401 `UNAUTHORIZED`, with `WWW-Authenticate` headers.
    * Update, simplify, and improve all the security docs.
    * Add new `scope_str` to `SecurityScopes` and update docs: OAuth2 scopes.
    * Update docs, images, tests.
    * PR #188.
  * Include Hypercorn as an alternative ASGI server in the docs. PR #187.
  * Add docs for Static Files and Templates. PR #186.
  * Add docs for handling Response Cookies and Response Headers. PR #185.
  * Fix typos in docs. PR #176 by @chdsbd.


## 0.19.0¶
  * Rename _path operation decorator_ parameter `content_type` to `response_class`. PR #183.
  * Add docs:
    * How to use the `jsonable_encoder` in JSON compatible encoder.
    * How to Return a Response directly.
    * Update how to use a Custom Response Class.
    * PR #184.


## 0.18.0¶
  * Add docs for HTTP Basic Auth. PR #177.
  * Upgrade HTTP Basic Auth handling with automatic headers (automatic browser login prompt). PR #175.
  * Update dependencies for security. PR #174.
  * Add docs for Middleware. PR #173.


## 0.17.0¶
  * Make Flit publish from CI. PR #170.
  * Add documentation about handling CORS (Cross-Origin Resource Sharing). PR #169.
  * By default, encode by alias. This allows using Pydantic `alias` parameters working by default. PR #168.


## 0.16.0¶
  * Upgrade _path operation_ `docstring` parsing to support proper Markdown descriptions. New documentation at Path Operation Configuration. PR #163.
  * Refactor internal usage of Pydantic to use correct data types. PR #164.
  * Upgrade Pydantic to version `0.23`. PR #160 by @euri10.
  * Fix typo in Tutorial about Extra Models. PR #159 by @danielmichaels.
  * Fix Query Parameters URL examples in docs. PR #157 by @hayata-yamamoto.


## 0.15.0¶
  * Add support for multiple file uploads (as a single form field). New docs at: Multiple file uploads. PR #158.
  * Add docs for: Additional Status Codes. PR #156.


## 0.14.0¶
  * Improve automatically generated names of _path operations_ in OpenAPI (in API docs). A function `read_items` instead of having a generated name "Read Items Get" will have "Read Items". PR #155.
  * Add docs for: Testing **FastAPI**. PR #151.
  * Update `/docs` Swagger UI to enable deep linking. This allows sharing the URL pointing directly to the _path operation_ documentation in the docs. PR #148 by @wshayes.
  * Update development dependencies, `Pipfile.lock`. PR #150.
  * Include Falcon and Hug in: Alternatives, Inspiration and Comparisons.


## 0.13.0¶
  * Improve/upgrade OAuth2 scopes support with `SecurityScopes`:
    * `SecurityScopes` can be declared as a parameter like `Request`, to get the scopes of all super-dependencies/dependants.
    * Improve `Security` handling, merging scopes when declaring `SecurityScopes`.
    * Allow using `SecurityBase` (like `OAuth2`) classes with `Depends` and still document them. `Security` now is needed only to declare `scopes`.
    * Updated docs about: OAuth2 with Password (and hashing), Bearer with JWT tokens.
    * New docs about: OAuth2 scopes.
    * PR #141.


## 0.12.1¶
  * Fix bug: handling additional `responses` in `APIRouter.include_router()`. PR #140.
  * Fix typo in SQL tutorial. PR #138 by @mostaphaRoudsari.
  * Fix typos in section about nested models and OAuth2 with JWT. PR #127 by @mmcloud.


## 0.12.0¶
  * Add additional `responses` parameter to _path operation decorators_ to extend responses in OpenAPI (and API docs).
    * It also allows extending existing responses generated from `response_model`, declare other media types (like images), etc.
    * The new documentation is here: Additional Responses.
    * `responses` can also be added to `.include_router()`, the updated docs are here: Bigger Applications.
    * PR #97 originally initiated by @barsi.
  * Update `scripts/test-cov-html.sh` to allow passing extra parameters like `-vv`, for development.


## 0.11.0¶
  * Add `auto_error` parameter to security utility functions. Allowing them to be optional. Also allowing to have multiple alternative security schemes that are then checked in a single dependency instead of each one verifying and returning the error to the client automatically when not satisfied. PR #134.
  * Update SQL Tutorial to close database sessions even when there are exceptions. PR #89 by @alexiri.
  * Fix duplicate dependency in `pyproject.toml`. PR #128 by @zxalif.


## 0.10.3¶
  * Add Gitter chat, badge, links, etc. https://gitter.im/tiangolo/fastapi . PR #117.
  * Add docs about Extending OpenAPI. PR #126.
  * Make Travis run Ubuntu Xenial (newer version) and Python 3.7 instead of Python 3.7-dev. PR #92 by @blueyed.
  * Fix duplicated param variable creation. PR #123 by @yihuang.
  * Add note in Response Model docs about why using a function parameter instead of a function return type annotation. PR #109 by @JHSaunders.
  * Fix event docs (startup/shutdown) function name. PR #105 by @stratosgear.


## 0.10.2¶
  * Fix OpenAPI (JSON Schema) for declarations of Python `Union` (JSON Schema `additionalProperties`). PR #121.
  * Update Background Tasks with a note on Celery.
  * Document response models using unions and lists, updated at: Extra Models. PR #108.


## 0.10.1¶
  * Add docs and tests for encode/databases. New docs at: Async SQL (Relational) Databases. PR #107.


## 0.10.0¶
  * Add support for Background Tasks in _path operation functions_ and dependencies. New documentation about Background Tasks is here. PR #103.
  * Add support for `.websocket_route()` in `APIRouter`. PR #100 by @euri10.
  * New docs section about Events: startup - shutdown. PR #99.


## 0.9.1¶
  * Document receiving Multiple values with the same query parameter and Duplicate headers. PR #95.


## 0.9.0¶
  * Upgrade compatible Pydantic version to `0.21.0`. PR #90.
  * Add documentation for: Application Configuration.
  * Fix typo in docs. PR #76 by @matthewhegarty.
  * Fix link in "Deployment" to "Bigger Applications".


## 0.8.0¶
  * Make development scripts executable. PR #76 by @euri10.
  * Add support for adding `tags` in `app.include_router()`. PR #55 by @euri10. Documentation updated in the section: Bigger Applications.
  * Update docs related to Uvicorn to use new `--reload` option from version `0.5.x`. PR #74.
  * Update `isort` imports and scripts to be compatible with newer versions. PR #75.


## 0.7.1¶
  * Update technical details about `async def` handling with respect to previous frameworks. PR #64 by @haizaar.
  * Add deployment documentation for Docker in Raspberry Pi and other architectures.
  * Trigger Docker images build on Travis CI automatically. PR #65.


## 0.7.0¶
  * Add support for `UploadFile` in `File` parameter annotations.
    * This includes a file-like interface.
    * Here's the updated documentation for declaring `File` parameters with `UploadFile`.
    * And here's the updated documentation for using `Form` parameters mixed with `File` parameters, supporting `bytes` and `UploadFile` at the same time.
    * PR #63.


## 0.6.4¶
  * Add technical details about `async def` handling to docs. PR #61.
  * Add docs for Debugging FastAPI applications in editors.
  * Clarify Bigger Applications deployed with Docker.
  * Fix typos in docs.
  * Add section about History, Design and Future.
  * Add docs for using WebSockets with **FastAPI**. PR #62.


## 0.6.3¶
  * Add Favicons to docs. PR #53.


## 0.6.2¶
  * Introduce new project generator based on FastAPI and PostgreSQL: https://github.com/tiangolo/full-stack-fastapi-postgresql. PR #52.
  * Update SQL tutorial with SQLAlchemy, using `Depends` to improve editor support and reduce code repetition. PR #52.
  * Improve middleware naming in tutorial for SQL with SQLAlchemy https://fastapi.tiangolo.com/tutorial/sql-databases/.


## 0.6.1¶
  * Add docs for GraphQL: https://fastapi.tiangolo.com/advanced/graphql/. PR #48.


## 0.6.0¶
  * Update SQL with SQLAlchemy tutorial at https://fastapi.tiangolo.com/tutorial/sql-databases/ using the new official `request.state`. PR #45.
  * Upgrade Starlette to version `0.11.1` and add required compatibility changes. PR #44.


## 0.5.1¶
  * Add section about helping and getting help with **FastAPI**.
  * Add note about path operations order in docs.
  * Update section about error handling with more information and make relation with Starlette error handling utilities more explicit. PR #41.
  * Add Development - Contributing section to the docs. PR #42.


## 0.5.0¶
  * Add new `HTTPException` with support for custom headers. With new documentation for handling errors at: https://fastapi.tiangolo.com/tutorial/handling-errors/. PR #35.
  * Add documentation to use Starlette `Request` object directly. Check #25 by @euri10.
  * Add issue templates to simplify reporting bugs, getting help, etc: #34.
  * Update example for the SQLAlchemy tutorial at https://fastapi.tiangolo.com/tutorial/sql-databases/ using middleware and database session attached to request.


## 0.4.0¶
  * Add `openapi_prefix`, support for reverse proxy and mounting sub-applications. See the docs at https://fastapi.tiangolo.com/advanced/sub-applications-proxy/: #26 by @kabirkhan.
  * Update docs/tutorial for SQLAlchemy including note about _DB Browser for SQLite_.


## 0.3.0¶
  * Fix/add SQLAlchemy support, including ORM, and update docs for SQLAlchemy: #30.


## 0.2.1¶
  * Fix `jsonable_encoder` for Pydantic models with `Config` but without `json_encoders`: #29.


## 0.2.0¶
  * Fix typos in Security section: #24 by @kkinder.
  * Add support for Pydantic custom JSON encoders: #21 by @euri10.


## 0.1.19¶
  * Upgrade Starlette version to the current latest `0.10.1`: #17 by @euri10.

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
