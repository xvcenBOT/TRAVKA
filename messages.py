# messages.py (fixed)
RU_TEXTS = {
    "start_message": (
        "<b>Добро пожаловать в TRAVKA OTC – надёжный P2P‑гарант</b>\n\n"
        "<b>💼 Покупайте и продавайте всё, что угодно — безопасно!</b>\n"
        "От Telegram‑подарков и NFT до токенов и фиата — сделки проходят легко и без риска.\n\n"
        "🔹 Удобное управление кошельками\n"
        "🔹 Реферальная система\n\n"
        "<b>📖 Как пользоваться?</b>\n"
        "Ознакомьтесь с инструкцией — https://telegra.ph/Podrobnyj-gajd-po-ispolzovaniyu-TravkaDeal-bot-09-13\n\n"
        "Выберите нужный раздел ниже:"
    ),
    "wallet_menu_message": "Выберите способ оплаты:",
    "add_ton_wallet_message": (
        "<b>💼 Ваш текущий TON‑кошелёк:</b> <code>{current_wallet}</code>\n\n"
        "Пожалуйста, отправьте новый адрес вашего кошелька."
    ),
    "add_card_message": (
        "<b>💳 Ваши текущие реквизиты:</b> <code>{current_card}</code>\n\n"
        "Пожалуйста, отправьте реквизиты в формате: <code>Банк - Номер карты</code>."
    ),
    "no_requisites_message": "❌ Сначала добавьте необходимые реквизиты перед созданием сделки.",
    "choose_payment_method_message": "<b>💰 Выберите метод получения оплаты:</b>",
    "create_deal_message": (
        "<b>💼 Создание сделки</b>\n\n"
        "Введите сумму в формате: <code>100.5</code>"
    ),
    "change_lang_message": "Сменить язык:",
    "awaiting_description_message": (
        "<b>📝 Укажите, что вы предлагаете в этой сделке:</b>\n\n"
        "<code>Пример: 10 кепок и Пепе</code>"
    ),
    "wallet_updated": "🔗 {wallet_type} обновлён: {details}",
    "deal_created_message": (
        "<b>✅ Сделка успешно создана!</b>\n\n"
        "💰 Сумма: {amount} {valute}\n"
        "📜 Описание: <b>{description}</b>\n"
        "🔗 Ссылка для покупателя: {deal_link}"
    ),
    "deal_info_ton_message": (
        "💳 Информация о сделке #{deal_id}\n\n"
        "👤 Вы покупатель в сделке.\n"
        "📌 Продавец: @{seller_username}\n"
        "• Успешные сделки: {successful_deals}\n\n"
        "• Вы покупаете: {description}\n\n"
        "🏦 Адрес для оплаты (TON): {wallet}\n\n"
        "💰 Сумма к оплате: {amount} TON\n"
        "📝 Комментарий к платежу (мемо): {deal_id}\n\n"
        "⚠️ Убедитесь в правильности данных перед оплатой. Комментарий (мемо) обязателен!\n\n"
        "После оплаты ожидайте подтверждения администратором."
    ),
    "deal_info_sbp_message": (
        "💳 Информация о сделке #{deal_id}\n\n"
        "👤 Вы покупатель в сделке.\n"
        "📌 Продавец: @{seller_username}\n"
        "• Успешные сделки: {successful_deals}\n\n"
        "• Вы покупаете: {description}\n\n"
        "💳 Карта для оплаты (РФ): {card}\n\n"
        "💰 Сумма к оплате: {amount} RUB\n"
        "📝 Комментарий к платежу: {deal_id}\n\n"
        "⚠️ Убедитесь в правильности данных перед оплатой. Комментарий обязателен!\n\n"
        "После оплаты ожидайте подтверждения администратором."
    ),
    "deal_info_stars_message": (
        "💳 Информация о сделке #{deal_id}\n\n"
        "👤 Вы покупатель в сделке.\n"
        "📌 Продавец: @{seller_username}\n"
        "• Успешные сделки: {successful_deals}\n\n"
        "• Вы покупаете: {description}\n\n"
        "🌟 Оплата через Telegram Stars: {command}\n\n"
        "💰 Сумма к оплате: {amount} Звёзд\n"
        "📝 Укажите комментарий: {deal_id}\n\n"
        "⚠️ Убедитесь в правильности данных перед оплатой. Комментарий обязателен!\n\n"
        "После оплаты ожидайте подтверждения администратором."
    ),
    "payment_confirmed_message": (
        "✅ Оплата подтверждена для сделки #{deal_id}.\n\n"
        "Пожалуйста, подтвердите получение подарка после того, как продавец его отправит."
    ),
    "payment_confirmed_seller_message": (
        "<b>✅ Оплата подтверждена для сделки</b> <code>#{deal_id}</code>.\n\n"
        "Сумма: {amount}\n"
        "Описание: {description}\n\n"
        "❗️<b>Пожалуйста, передайте NFT‑подарок.</b>\n"
        "<b><u>Только холдеру бота для обработки:</u></b>\n"
        "@travkadeal_support\n\n"
        "⚠️ <b><u>Обратите внимание:</u></b>\n"
        "➤ <b>Подарок необходимо передать именно холдеру @travkadeal_support а не покупателю напрямую.</b>\n"
        "➤ Это стандартный процесс для автоматического завершения сделки через бота.\n\n"
        "После отправки подарка холдеру подтвердите действие кнопкой ниже:"
    ),
    "seller_confirm_sent_message": (
        "✅ Вы подтвердили отправку подарка для сделки #{deal_id}.\n"
        "Ожидайте подтверждения получения от покупателя."
    ),
    "seller_confirm_sent_notification": (
        "🎁 Продавец @{seller_username} (https://t.me/{seller_username}) подтвердил отправку подарка для сделки #{deal_id}.\n\n"
        "Пожалуйста, подтвердите его получение."
    ),
    "buyer_confirm_received_message": (
        "✅ Сделка #{deal_id} завершена.\n\n"
        "Спасибо за использование нашего сервиса."
    ),
    "seller_notification_message": (
        "👤 Пользователь @{buyer_username} присоединился к сделке #{deal_id}\n"
        "• Успешные сделки: {successful_deals}\n\n"
        "⚠️ Проверьте, что это тот же пользователь, с которым вы вели диалог ранее!"
    ),
    "insufficient_balance_message": "❌ Недостаточно средств на балансе!",
    "admin_panel_message": "🔧 Админ‑панель:",
    "admin_broadcast_message": "📢 Введите текст для рассылки всем пользователям:",
    "broadcast_success_message": (
        "📢 Рассылка завершена.\n"
        "✅ Успешно отправлено: {success_count}\n"
        "❌ Ошибок: {fail_count}"
    ),
    "admin_view_deals_message": "💳 Выберите сделку:\n{deals_list}",
    "admin_view_deal_message": (
        "<b>ℹ️ Информация о сделке #{deal_id}</b>\n\n"
        "👤 <b>Продавец:</b> @{seller_username} (ID: <code>{seller_id}</code>)\n"
        "✅ Успешных сделок: {seller_successful_deals}\n\n"
        "👤 <b>Покупатель:</b> @{buyer_username} (ID: <code>{buyer_id}</code>)\n"
        "✅ Успешных сделок: {buyer_successful_deals}\n\n"
        "➖➖➖➖➖➖➖➖➖➖\n\n"
        "📝 <b>Описание:</b>\n{description}\n\n"
        "💰 <b>Сумма:</b> {amount} {valute}\n"
        "💳 <b>Реквизиты для оплаты:</b>\n<code>{payment_details}</code>\n\n"
        "📊 <b>Статус:</b> {status}"
    ),
    "admin_confirm_deal_message": (
        "✅ Оплата для сделки #{deal_id} подтверждена администратором.\n"
        "Продавец и покупатель уведомлены."
    ),
    "admin_cancel_deal_message": "❌ Сделка #{deal_id} была отменена администратором.",
    "deal_cancelled_notification": "❌ Сделка #{deal_id} была отменена администратором.",
    "admin_change_balance_message": "Введите ID пользователя и новый баланс в формате: user_id баланс",
    "admin_change_successful_deals_message": "Введите ID пользователя и количество успешных сделок в формате: user_id количество",
    "admin_change_valute_message": "Введите новую валюту (например, USD, EUR, RUB):",
    "admin_manage_admins_message": "Введите ID пользователя и действие (add/remove) в формате: user_id действие",
    "admin_added_message": "✅ Пользователь {user_id} добавлен в администраторы.",
    "admin_removed_message": "❌ Пользователь {user_id} удалён из администраторов.",
    "admin_cannot_remove_self_message": "🚫 Вы не можете удалить себя из администраторов!",
    "admin_cannot_remove_super_admin_message": "🚫 Нельзя удалить суперадминистратора.",
    "invalid_action_message": "❌ Неверное действие. Используйте 'add' или 'remove'.",
    "admin_list_message": "👑 Список администраторов:\n\n{admin_list}",
    "unknown_callback_error": "❌ Неизвестное действие. Пожалуйста, выберите опцию из меню.",
    "lang_set_message": "✅ Язык изменён на Русский.",
    "referral_message": (
        "🧷 Ваша реферальная ссылка: <code>{referral_link}</code>\n\n"
        "Приглашайте друзей и получайте бонусы за их сделки!"
    ),
    "menu_button": "🔙 Вернуться в меню",
    "pay_from_balance_button": "💸 Оплатить с баланса",
    "add_wallet_button": "🪙 Добавить/изменить кошелёк",
    "add_ton_wallet_button": "💼 Добавить/изменить TON‑кошелёк",
    "add_card_button": "💳 Добавить/изменить карту",
    "create_deal_button": "📄 Создать сделку",
    "referral_button": "🧷 Реферальная ссылка",
    "change_lang_button": "🌐 Change language",
    "support_button": "📞 Поддержка",
    "english_lang_button": "🇬🇧 English",
    "russian_lang_button": "🇷🇺 Русский",
    "admin_view_deals_button": "💳 Просмотр сделок",
    "admin_change_balance_button": "💰 Изменить баланс пользователя",
    "admin_change_successful_deals_button": "✅ Изменить успешные сделки",
    "admin_change_valute_button": "💱 Изменить валюту",
    "admin_manage_admins_button": "👑 Назначить/удалить администратора",
    "admin_list_button": "👑 Список администраторов",
    "admin_confirm_deal_button": "✅ Подтвердить",
    "admin_cancel_deal_button": "❌ Отменить",
    "seller_confirm_sent_button": "✅Подтвердить отправку",
    "contact_support_button": "Тех. поддержка",
    "payment_ton_button": "На TON‑кошелёк",
    "payment_sbp_button": "Карта (РФ)",
    "payment_stars_button": "Звёзды",
    "not_specified_wallet": "не указан",
    "not_specified_card": "не указаны",
    "critical_rule_message": (
        "🛡️<b>Критически важное правило:</b>\n"
        "<b>Подарок должен быть передан исключительно холдеру</b>\n"
        "👉 @travkadeal_support\n\n"
        "🚫 <b>Если вам предлагают нарушить процедуру:</b>\n"
        "• «Передайте напрямую покупателю/другому лицу» →\n"
        "• Это мошенническая схема!\n"
        "• Любая передача мимо холдера:\n"
        "  - Автоматически отменяет сделку\n"
        "  - Лишает гарантий возврата средств"
    ),
}

EN_TEXTS = {
    "start_message": (
        "<b>Welcome to TRAVKA OTC – a reliable P2P guarantor</b>\n\n"
        "<b>💼 Buy and sell anything — safely!</b>\n"
        "From Telegram gifts and NFTs to tokens and fiat — transactions are easy and risk‑free.\n\n"
        "🔹 Convenient wallet management\n"
        "🔹 Referral system\n\n"
        "Choose the desired section below:"
    ),
    "wallet_menu_message": "Select payment method:",
    "add_ton_wallet_message": (
        "💼 Your current TON wallet: <code>{current_wallet}</code>\n\n"
        "Please send the new wallet address."
    ),
    "add_card_message": (
        "💳 Your current card details: <code>{current_card}</code>\n\n"
        "Please send the card details in the format: <code>Bank - Card Number</code>."
    ),
    "no_requisites_message": "❌ Please add payment details before creating a deal.",
    "choose_payment_method_message": "💰 Select payment method:",
    "create_deal_message": (
        "💼 Create a deal\n\n"
        "Enter the amount in the format: <code>100.5</code>"
    ),
    "change_lang_message": "Change Language:",
    "awaiting_description_message": (
        "📝 Specify what you are offering in this deal:\n\n"
        "<code>Example: 10 caps and Pepe</code>"
    ),
    "wallet_updated": "🔗 {wallet_type} updated: {details}",
    "deal_created_message": (
        "✅ Deal successfully created!\n\n"
        "💰 Amount: {amount} {valute}\n"
        "📜 Description: {description}\n"
        "🔗 Buyer link: {deal_link}"
    ),
    "deal_info_ton_message": (
        "💳 Deal information #{deal_id}\n\n"
        "👤 You are the buyer in this deal.\n"
        "📌 Seller: @{seller_username}\n"
        "• Successful deals: {successful_deals}\n\n"
        "• You are buying: {description}\n\n"
        "🏦 Payment address (TON): {wallet}\n\n"
        "💰 Amount to pay: {amount} TON\n"
        "📝 Payment comment (memo): {deal_id}\n\n"
        "⚠️ Ensure the data is correct before payment. The comment (memo) is mandatory!\n\n"
        "After payment, wait for admin confirmation."
    ),
    "deal_info_sbp_message": (
        "💳 Deal information #{deal_id}\n\n"
        "👤 You are the buyer in this deal.\n"
        "📌 Seller: @{seller_username}\n"
        "• Successful deals: {successful_deals}\n\n"
        "• You are buying: {description}\n\n"
        "💳 Card for payment (Russia): {card}\n\n"
        "💰 Amount to pay: {amount} RUB\n"
        "📝 Payment comment: {deal_id}\n\n"
        "⚠️ Ensure the data is correct before payment. The comment is mandatory!\n\n"
        "After payment, wait for admin confirmation."
    ),
    "deal_info_stars_message": (
        "💳 Deal information #{deal_id}\n\n"
        "👤 You are the buyer in this deal.\n"
        "📌 Seller: @{seller_username}\n"
        "• Successful deals: {successful_deals}\n\n"
        "• You are buying: {description}\n\n"
        "🌟 Payment via Telegram Stars: {command}\n\n"
        "💰 Amount to pay: {amount} Stars\n"
        "📝 Specify comment: {deal_id}\n\n"
        "⚠️ Ensure the data is correct before payment. The comment is mandatory!\n\n"
        "After payment, wait for admin confirmation."
    ),
    "payment_confirmed_message": (
        "✅ Payment confirmed for deal #{deal_id}.\n\n"
        "Please confirm receipt of the gift after the seller sends it."
    ),
    "payment_confirmed_seller_message": (
        "✅ Payment confirmed for deal #{deal_id}.\n\n"
        "Amount: {amount}\n"
        "Description: {description}\n\n"
        "❗️ Please transfer the NFT‑gift to the bot <b>holder</b> for processing:\n"
        "Only to the <b>holder</b>:\n"
        "@travkadeal_support\n\n"
        "⚠️ Note:\n"
        "➤ Transfer must be made to the holder @travkadeal_support not directly to the buyer.\n"
        "➤ This is the standard procedure for automatic deal completion via the bot.\n\n"
        "After sending to the holder,\n"
        "confirm the action with the button below:"
    ),
    "seller_confirm_sent_message": (
        "✅ You confirmed sending the gift for deal #{deal_id}.\n"
        "Waiting for the buyer's confirmation of receipt."
    ),
    "seller_confirm_sent_notification": (
        "🎁 Seller @{seller_username} (https://t.me/{seller_username}) confirmed sending the gift for deal #{deal_id}.\n\n"
        "Please confirm its receipt."
    ),
    "buyer_confirm_received_message": (
        "✅ Deal #{deal_id} completed.\n\n"
        "Thank you for using our service."
    ),
    "seller_notification_message": (
        "👤 User @{buyer_username} has joined the deal #{deal_id}\n"
        "• Successful deals: {successful_deals}\n\n"
        "⚠️ Make sure this is the same user you were talking to earlier!"
    ),
    "insufficient_balance_message": "❌ Insufficient balance!",
    "admin_panel_message": "🔧 Admin panel:",
    "admin_broadcast_message": "📢 Enter the text for broadcasting to all users:",
    "broadcast_success_message": (
        "📢 Broadcast completed.\n"
        "✅ Successfully sent: {success_count}\n"
        "❌ Errors: {fail_count}"
    ),
    "admin_view_deals_message": "💳 Select a deal:\n{deals_list}",
    "admin_view_deal_message": (
        "<b>ℹ️ Deal Information #{deal_id}</b>\n\n"
        "👤 <b>Seller:</b> @{seller_username} (ID: <code>{seller_id}</code>)\n"
        "✅ Successful deals: {seller_successful_deals}\n\n"
        "👤 <b>Buyer:</b> @{buyer_username} (ID: <code>{buyer_id}</code>)\n"
        "✅ Successful deals: {buyer_successful_deals}\n\n"
        "➖➖➖➖➖➖➖➖➖➖\n\n"
        "📝 <b>Description:</b>\n{description}\n\n"
        "💰 <b>Amount:</b> {amount} {valute}\n"
        "💳 <b>Payment Details:</b>\n<code>{payment_details}</code>\n\n"
        "📊 <b>Status:</b> {status}"
    ),
    "admin_confirm_deal_message": (
        "✅ Payment for deal #{deal_id} confirmed by admin.\n"
        "Seller and buyer have been notified."
    ),
    "admin_cancel_deal_message": "❌ Deal #{deal_id} was cancelled by admin.",
    "deal_cancelled_notification": "❌ Deal #{deal_id} was cancelled by admin.",
    "admin_change_balance_message": "Enter user ID and new balance in the format: user_id balance",
    "admin_change_successful_deals_message": "Enter user ID and number of successful deals in the format: user_id count",
    "admin_change_valute_message": "Enter new currency (e.g., USD, EUR, RUB):",
    "admin_manage_admins_message": "Enter user ID and action (add/remove) in the format: user_id action",
    "admin_added_message": "✅ User {user_id} has been added as an admin.",
    "admin_removed_message": "❌ User {user_id} has been removed from admins.",
    "admin_cannot_remove_self_message": "🚫 You cannot remove yourself from admins!",
    "admin_cannot_remove_super_admin_message": "🚫 Cannot remove a super admin.",
    "invalid_action_message": "❌ Invalid action. Use 'add' or 'remove'.",
    "admin_list_message": "👑 List of administrators:\n\n{admin_list}",
    "unknown_callback_error": "❌ Unknown action. Please select an option from the menu.",
    "lang_set_message": "✅ Language changed to English.",
    "referral_message": (
        "🧷 Your referral link: <code>{referral_link}</code>\n\n"
        "Invite friends and earn bonuses for their deals!"
    ),
    "menu_button": "🔙 Back to menu",
    "pay_from_balance_button": "💸 Pay from balance",
    "add_wallet_button": "🪙 Add/change wallet",
    "add_ton_wallet_button": "💼 Add/change TON wallet",
    "add_card_button": "💳 Add/change card",
    "create_deal_button": "📄 Create deal",
    "referral_button": "🧷 Referral link",
    "change_lang_button": "🌐 Change language",
    "support_button": "📞 Support",
    "english_lang_button": "🇬🇧 English",
    "russian_lang_button": "🇷🇺 Русский",
    "admin_view_deals_button": "💳 View deals",
    "admin_change_balance_button": "💰 Change user balance",
    "admin_change_successful_deals_button": "✅ Change successful deals",
    "admin_change_valute_button": "💱 Change currency",
    "admin_manage_admins_button": "👑 Appoint/remove admin",
    "admin_list_button": "👑 List of administrators",
    "admin_confirm_deal_button": "✅ Confirm",
    "admin_cancel_deal_button": "❌ Cancel",
    "seller_confirm_sent_button": "✅Confirm sending",
    "contact_support_button": "Tech Support",
    "payment_ton_button": "To TON wallet",
    "payment_sbp_button": "Via RU CARD",
    "payment_stars_button": "Stars",
    "not_specified_wallet": "not specified",
    "not_specified_card": "not specified",
    "critical_rule_message": (
        "🛡️ Critical rule:\n"
        "The gift must be transferred exclusively to the <b>holder</b>\n"
        "👉 @travkadeal_support\n\n"
        "🚫 If someone asks you to break the procedure:\n"
        "• \"Transfer directly to the buyer/another person\" →\n"
        "• This is a scam!\n"
        "• Any transfer bypassing the holder:\n"
        "  - Will automatically cancel the deal\n"
        "  - Will void refund guarantees"
    ),
}

def get_text(lang, key, **kwargs):
    texts_to_use = RU_TEXTS if lang == 'ru' else EN_TEXTS
    message_template = texts_to_use.get(key, '')

    if not message_template and lang == 'ru':
        message_template = EN_TEXTS.get(key, '')
    elif not message_template and lang == 'en':
        message_template = RU_TEXTS.get(key, '')

    if not message_template:
        print(f"Warning: Text key '{key}' not found for language '{lang}' or fallback.")
        return f"Error: Text for '{key}' not found."

    try:
        return message_template.format(**kwargs)
    except KeyError as e:
        print(f"Warning: Missing placeholder {e} for key '{key}' in lang '{lang}'. Provided kwargs: {kwargs}")
        return f"Error: Text for '{key}' has missing data."
    except Exception as e:
        print(f"Error formatting text for key '{key}', lang '{lang}': {e}")
        return "Error: Could not format message."
